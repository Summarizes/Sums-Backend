# Table Of Content
|API Name|Method|Endpoint|Description
|-----|---------|-------------|------|
|1. Account
|สร้าง Account|**POST**|`/accounts` 
|ดูข้อมูล Account|**GET**|`/accounts/:account_id`
|แก้ไข Account|**PUT**|`/accounts/:account_id`
|ลบ Account|**DELETE**|`/accounts/:account_id`
|2. Payment Method
|ดูบัญชีธนคาร|**GET**|`/accounts/:account_id/bank-account`
|สร้างบัญชีธนคาร|**POST**|`/accounts/:account_id/bank-account`
|แก้ไขบัญชีธนคาร|**PUT**|`/accounts/:account_id/bank-account`
|ลบบัญชีธนคาร|**DELETE**|`/accounts/:account_id/bank-account`
|3. Bundle
|ดูข้อมูล Bundle|**GET**|`/bundles/:bundle_id`
|ดูข้อมูล Bundle ทั้งหมดของ Account|**GET**|`/accounts/:account_id/bundles`
|สร้าง Bundle พร้อมไฟล์ที่จะขาย|**POST**|`/accounts/:account_id/bundles`
|แก้ไข Bundle (แก้ไขไฟล์ยังไม่ได้)|**PUT**|` /accounts/:account_id/bundles/:bundle_id`
|ลบ Bundle พร้อมไฟล์|**DELETE**|`/accounts/:account_id/bundles/:bundle_id`
|4. File
|ดูข้อมูลไฟล์|**GET**|`/files/:file_id`
|แก้ข้อมูลไฟล์|**PUT**|`/files/:file_id`
|ลบไฟล์|**DELETE**|`/files/:file_id`
|5. Payment
|ดูประวัติการซื้อ|**GET**|`/payments/:payment_id`
|ดูประวัติการซื้อทั้งหมดของ Account|**GET**|`/accounts/:account_id/payments`
|สั่งซื้อ Bundle|**POST**|`/accounts/:account_id/payments/:bundle_id`
# Account
## **`POST`** สร้าง Account  
`/accounts`  

<!-- **Request**
```
{
  "username": INTEGER
  "password": INTEGER
  "firstname": INTEGER
  "lastname": INTEGER
}
``` -->



## **`PUT`** แก้ไข Account  
`/accounts/:account_id`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`GET`** ดูข้อมูล Account  
`/accounts/:account_id`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

# Payment Method
## **`POST`** สร้างบัญชีธนคาร  
`/accounts/:account_id/bank-account`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`PUT`** แก้ไขบัญชีธนคาร  
`/accounts/:account_id/bank-account`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`GET`** ดูบัญชีธนคาร  
`/accounts/:account_id/bank-account`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|



# Bundle
## **`GET`** ดูข้อมูล Bundle ทั้งหมดของ Account  
`/account/:account_id/bundles`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`GET`** ดูข้อมูล Bundle  
`/bundles/:bundle_id`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`bundle_id`|INTEGER|None|

## **`GET`** สร้าง Bundle พร้อมไฟล์ที่จะขาย  
`/accounts/:account_id/bundles`
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`GET`** แก้ไข Bundle (แก้ไขไฟล์ยังไม่ได้)  
` /accounts/:account_id/bundles/:bundle_id`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|
`bundle_id`|INTEGER|None|

## **`DELETE`** ลบ Bundle พร้อมไฟล์  
`/accounts/:account_id/bundles/:bundle_id`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|
`bundle_id`|INTEGER|None|


# Payment
## **`POST`** ซื้อไฟล์  
`/accounts/:account_id/payments`   
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`GET`** ดูประวัติการซื้อทั้งหมด  
`/accounts/:account_id/payments`  
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|

## **`GET`** ดูประวัติการซื้อ  
`/accounts/:account_id/payments/:payment_id`
**Params**
|Param|Type|Default|Description
|---------|-------------|------| --------|
`account_id`|INTEGER|None|
`payment_id`|INTEGER|None|
