# Account
**POST** สร้าง Account  
 `/accounts`

**PUT** แก้ไข Account  
  `/accounts/:account_id`

**GET** ดูข้อมูล Account  
  `/accounts/:account_id`


# Payment Method
**POST** สร้างบัญชีธนคาร  
  `/accounts/:account_id/bank-account`

**PUT** แก้ไขบัญชีธนคาร  
   `/accounts/:account_id/bank-account`

**GET** ดูบัญชีธนคาร  
   `/accounts/:account_id/bank-account`



# Bundle
**GET** ดูข้อมูล Bundle ทั้งหมดของ Account  
  `/account/:account_id/bundles`

**GET** ดูข้อมูล Bundle  
  `/bundles/:bundle_id`

**GET** สร้าง Bundle พร้อมไฟล์ที่จะขาย  
  `/accounts/:account_id/bundles`

**GET** แก้ไข Bundle (แก้ไขไฟล์ยังไม่ได้)  
   ` /accounts/:account_id/bundles/:bundle_id`

**DELETE** ลบ Bundle พร้อมไฟล์  
 `/accounts/:account_id/bundles/:bundle_id`


# Payment
**POST** ซื้อไฟล์  
   `/accounts/:account_id/payments`  

**GET** ดูประวัติการซื้อทั้งหมด  
    `/accounts/:account_id/payments ` 

**GET** ดูประวัติการซื้อ  
    `/accounts/:account_id/payments/:payment_id`
