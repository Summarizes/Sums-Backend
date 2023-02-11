# Account
## **`POST`** Create Account  
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
