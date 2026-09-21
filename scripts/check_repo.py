"""Dependency-free checks for this repository's documentation and shot example."""

import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets.extend(value for key, value in attrs if key in ('href', 'src') and value)


def check(root):
    root = root.resolve()
    errors = []
    documents = sorted(p for p in root.rglob('*.md') if '.git' not in p.parts)
    links = 0
    for path in documents:
        text = path.read_text(encoding='utf-8')
        if len(re.findall(r'^```', text, re.M)) % 2:
            errors.append(f'{path.relative_to(root)}: unclosed fenced block')
        prose = re.sub(r'^```.*?^```[^\n]*', '', text, flags=re.M | re.S)
        html = References()
        html.feed(prose)
        targets = re.findall(r'\]\(([^\s)]+)\)', prose) + html.targets
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            links += 1
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f'{path.relative_to(root)}: missing/escaping reference {target}')
    example = root / 'examples/jade-seal-48s.md'
    if not example.is_file():
        errors.append('missing six-shot example')
    else:
        text = example.read_text(encoding='utf-8')
        rows = re.findall(r'^\| (S\d{2}) \| (\d{2}):(\d{2})–(\d{2}):(\d{2}) \| ([LZ]01): “([^”]+)”', text, re.M)
        if [row[0] for row in rows] != [f'S{i:02}' for i in range(1, 7)]:
            errors.append('expected six ordered storyboard rows S01–S06')
        end = 0
        for shot, sm, ss, em, es, speaker, dialogue in rows:
            start, finish = int(sm) * 60 + int(ss), int(em) * 60 + int(es)
            if start != end or finish - start != 8:
                errors.append(f'{shot}: timeline gap or duration is not 8 seconds')
            end = finish
            blocks = re.findall(r'```text\n(Shot ' + shot + r'\..*?)\n```', text, re.S)
            if len(blocks) != 1 or f'"{dialogue}"' not in blocks[0]:
                errors.append(f'{shot}: missing self-contained prompt or changed dialogue')
            elif ('Only Lin speaks' if speaker == 'L01' else 'Only Zhao speaks') not in blocks[0]:
                errors.append(f'{shot}: speaker does not match the script')
        if end != 48:
            errors.append('storyboard must end at 48 seconds')
    hero = root / 'assets/hero.png'
    if not hero.is_file():
        errors.append('missing hero asset')
    else:
        header = hero.read_bytes()[:24]
        if len(header) != 24 or header[:8] != b'\x89PNG\r\n\x1a\n':
            errors.append('hero is not a PNG')
        else:
            width, height = struct.unpack('>II', header[16:24])
            if width < 1000 or not 2.5 <= width / height <= 3.1:
                errors.append('hero must be a wide high-resolution banner')
    return errors, len(documents), links


if __name__ == '__main__':
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors, documents, links = check(root)
    for error in errors:
        print('FAIL:', error)
    if not errors:
        print(f'PASS: {documents} Markdown files; {links} local references; 6 shot prompts; 48s timeline; PNG banner')
    sys.exit(bool(errors))
