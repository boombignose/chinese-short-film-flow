# ลองหนึ่งช็อตก่อน — ตราหยกปริศนา

เริ่มจากตัวอย่าง 8 วินาทีนี้เพื่อเรียนรู้หน้าสร้างวิดีโอและการตรวจเสียง ก่อนทำ [ตอนเต็ม 6 ช็อต](jade-seal-48s.md)

| ตั้งค่า | ค่าเป้าหมาย |
|---|---|
| เครื่องมือ | Google Flow |
| โหมด | Video / Frames โดยไม่ใส่เฟรม เพื่อทดสอบข้อความเป็นวิดีโอ |
| โมเดล | Veo 3.1 Lite หรือรุ่นที่บัญชีรองรับ |
| อัตราส่วน / เวลา / จำนวน | 9:16 / 8 วินาที / x1 |
| เสียง | ผู้หญิงหนึ่งคนพูดไทย ผู้ชายเงียบ |

ตรวจราคาเครดิตจริงใน UI ก่อนกดสร้าง โหมดและชื่อเมนูอาจเปลี่ยนได้ ตัวอย่างนี้ทดสอบการสร้างช็อตเดี่ยว ยังไม่ทดสอบการคงหน้าข้ามช็อตเพราะไม่ได้ใช้ภาพอ้างอิง

## 1. คัดลอกไปวางใน Google Flow

```text
Create one continuous 8-second vertical 9:16 cinematic shot for an original fictional Chinese period mystery drama. Two adult characters in a red wooden archive hall at night. Lin Yue, a Chinese woman aged 26, oval face, brown eyes, half-up long black hair with a silver bamboo-leaf hairpin, pale jade-green hanfu and a white outer robe, no earrings, stands on screen-left. Zhao Yan, a Chinese man aged 30, angular clean-shaven face, high black topknot with a small silver crown, dark navy robe with silver trim, stands on screen-right. Warm amber lantern light from the left and cool moonlight from the right. Medium two-shot with a slow subtle camera push-in. Lin holds a round jade seal in her RIGHT hand at chest height and looks directly at Zhao. Only Lin speaks, in a calm medium-low female voice, exactly in Thai: "ตรานี้ บอกว่าท่านตายไปแล้ว". Zhao stays silent with his mouth closed and reacts with surprise. Brief pause before the line; hold their eye contact afterward. Quiet indoor ambience, no music, no narrator, no other speech, no text, no subtitles, no extra people. Keep the seal in Lin's right hand throughout. End on the man's silent reaction without a cut.
```

## 2. ตรวจผล

- แนวตั้ง 9:16 และเปิดเล่นได้ครบ
- มีผู้ใหญ่สองคน ผู้หญิงซ้าย ผู้ชายขวา ไม่มีบุคคลที่สาม
- ตราหยกอยู่มือขวาของผู้หญิง ไม่มีการสลับมือ
- ผู้หญิงพูดเพียงประโยคที่กำหนด ผู้ชายไม่พูดหรือขยับปากตาม
- ไม่มีซับจากการเจนติดภาพ และไม่มีเสียงพูดอื่น

ถ้าภาพผ่านแต่เสียงผิด ให้ใช้ [พรอมป์ต์แก้เสียง](../prompts/REPAIR.md) พร้อมระบุคำที่ผิด ห้ามสรุปว่าผ่านจากสถานะการเจนอย่างเดียว

## 3. ไปต่อเป็นตอนเต็ม

เมื่อช็อตเดี่ยวผ่าน ให้สร้างภาพอ้างอิงตัวละคร แล้วใช้ [ตราหยกใต้โคมแดง 48 วินาที](jade-seal-48s.md) เพื่อทดสอบความต่อเนื่อง 6 ช็อต

## ผลทดลองจริง

สร้างหนึ่งครั้งด้วย Veo 3.1 Lite ได้ไฟล์ 8 วินาที 720 × 1280 พร้อมเสียง: [ดู MP4](../assets/demo.mp4)

เป็น take ทดลองที่ยังไม่ผ่าน QC ทุกข้อ: ตราหยกมีรูปทรงยาวแทนวงกลม ปลายคลิปผู้ชายอ้าปาก และระบบถอดเสียงตรวจพบคำที่อาจเกินบท ต้องฟังยืนยันก่อนตัดสินคุณภาพเสียง อ่านหลักฐานและข้อจำกัดใน [รายงานทดสอบ](../docs/TEST-REPORT.md)

หากจะลองแก้ ให้เปลี่ยนทีละจุด เช่นเฟรมใกล้เฉพาะผู้หญิงเพื่อจำกัดผู้พูด หรือแนบภาพตราหยกรูปวงกลมจริง การเปลี่ยนพรอมป์ต์นี้ยังไม่ได้รันซ้ำและไม่รับประกันผล
