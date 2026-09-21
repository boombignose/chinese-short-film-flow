# ใช้กับ Claude

1. สร้าง Project ใหม่สำหรับหนังหนึ่งเรื่อง
2. วาง `prompts/MASTER-PROMPT.md` ใน Project instructions
3. เพิ่ม `WORKFLOW.md`, `templates/PRODUCTION.md` และ `examples/jade-seal-48s.md` ในความรู้ของโปรเจกต์
4. ใช้ข้อความเริ่มงานเดียวกับ README แล้วเลือกเรื่อง ให้ Claude ทำบรีฟ character bible บท storyboard และพรอมป์ต์
5. นำพรอมป์ต์ภาพไปสร้างใน Google Flow เลือก reference แล้วสร้างวิดีโอทีละช็อต

Claude Projects ใช้ความรู้และคำสั่งของโปรเจกต์เป็นบริบทได้ ดู [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects) ถ้าบัญชีไม่มี Projects ให้ใช้แชตพร้อมแนบไฟล์หรือวางข้อความแทน

## Claude Code หรือ agent ที่อ่านโฟลเดอร์ได้

เปิดโฟลเดอร์ repo แล้วให้ agent อ่าน `CLAUDE.md` ไฟล์นี้ชี้ไปยัง workflow และ prompt กลาง จากนั้นสร้างเอกสารของเรื่องใหม่ในโฟลเดอร์แยก ไม่แก้ไฟล์ตัวอย่างให้กลายเป็นงานจริง

`CLAUDE.md` สำหรับ Claude Code ไม่ได้กลายเป็นคำสั่ง Project โดยอัตโนมัติใน claude.ai ให้คัดลอก master prompt ตามขั้นตอนข้างต้น

## Claude ที่มี browser/computer tools

ใช้ `prompts/OPERATOR.md` หลังตรวจว่ามีเครื่องมือและสิทธิ์จริง การมี Claude Desktop หรือ repo อย่างเดียวไม่ยืนยันว่ากด Google Flow ได้ ถ้าไม่มีเครื่องมือ ให้ส่งชุดพรอมป์ต์สำหรับคัดลอกแทนการรายงานว่าเจนแล้ว

repo ไม่สมมติว่า Claude มีเครื่องมือสร้างภาพหรือวิดีโอในทุกบัญชี จึงใช้ Flow เป็นเส้นทางหลักสำหรับสร้างสื่อ

ตรวจแนวทางวันที่ 21 กันยายน 2026 ส่วน Claude เป็นการประยุกต์เพิ่มเติมจากคลิป ยังไม่ได้ทดสอบเจนสื่อผ่าน Claude ในบัญชีผู้ใช้
