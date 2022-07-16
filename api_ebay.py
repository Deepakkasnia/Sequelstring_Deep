import requests
import json
import time
from datetime import datetime, timedelta
now = datetime.now()
current_time = now.strftime("%H:%M:%S") 
print(current_time)

# url = " https://gstsandbox.charteredinfo.com/ewaybillapi/dec/v1.03/auth?action=ACCESSTOKEN&aspid=1683991922&password=Sequelstring@123&gstin=34AACCC1596Q002&username=TaxProEnvPON&ewbpwd=abc34*"
# result = {}
# res = requests.(url, data=json.dumps(result))
# result = json.loads(res.text)
# print(data)
# print(type(result["result"]))
# print(result["result"][0])
# print(result["result"])
# data={
# "supplyType":"O",
# "subSupplyType":"1",
# "subSupplyDesc":" ",
# "docType":"INV",
# -,"docNo":"111-1328",
# "docDate":"17/12/2017",
# "fromGstin":"34AACCC1596Q002",
# "fromTrdName":"welton",
# "fromAddr1":"2ND CROSS NO 59  19  A",
# "fromAddr2":"GROUND FLOOR OSBORNE ROAD",
# "fromPlace":"FRAZER TOWN",
# "fromPincode":605001,
# "actFromStateCode":34,
# "fromStateCode":34,
# "toGstin":"29AACCC1596Q000",
# "toTrdName":"sthuthya",
# "toAddr1":"Shree Nilaya",
# "toAddr2":"Dasarahosahalli",
# "toPlace":"Beml Nagar",
# "toPincode":562160,
# "actToStateCode":29,
# "toStateCode":29,
# "transactionType":4,
# "dispatchFromGSTIN":"29AACCC1596Q000",
# "dispatchFromTradeName":"ABC Traders",
# "shipToGSTIN":"29ALSPR1722R1Z3",
# "shipToTradeName":"XYZ Traders",
# "otherValue": -100,
# "totalValue":56099,
# "cgstValue":0,
# "sgstValue":0,
# "igstValue":300.67,
# "cessValue":400.56,
# "cessNonAdvolValue":400,
# "totInvValue":68358,
# "transporterId":"",
# "transporterName":"",
# "transDocNo":"",
# "transMode":"1",
# "transDistance":"0",
# "transDocDate":"",
# "vehicleNo":"PVC1234",
# "vehicleType":"R",
# "itemList":[{
# "productName":"Wheat",
# "productDesc":"Wheat",
# "hsnCode":1001,
# "quantity":4,
# "qtyUnit":"BOX",
# "cgstRate":0,
# "sgstRate":0,
# "igstRate":3,
# "cessRate":0,
# "cessNonAdvol":0,
# "taxableAmount":56099
# }]
# }

# url = "https://gstsandbox.charteredinfo.com/ewaybillapi/dec/v1.03/ewayapi?action=GENEWAYBILL&aspid=1683991922&password=Sequelstring@123&gstin=34AACCC1596Q002&username=TaxProEnvPON&authtoken=tqHArHh2L5dhuAu1jcPxkO48g"
# # data={"CID":data}
# res = requests.post(url, data=json.dumps(data))
# # print(res.text)

# data = json.loads(res.text)
# print(data)
# # print(type(data["result"][0]))
# print("\n------------------------------------------")
# print(data["ewayBillNo"],"ye hmara eway bill no h ")
# print(data["ewayBillDate"],"date of generation:_")
# # return data["result"]

####------get*api-----######

 
url = f"http://gstsandbox.charteredinfo.com/ewaybillapi/dec/v1.03/ewayapi?action=GetEwayBillGeneratedByConsigner&aspid=1683991922&password=Sequelstring@123&gstin=34AACCC1596Q002&username=TaxProEnvPON&authtoken=vYNJHccs08HTWVMUaMZrVfwQ7&docType={docType}&docNo={docNo}"
result = {}
res = requests.get(url, data=json.dumps(result))
result = json.loads(res.text)
# print(result)
print(result["ewayBillNo"],"<---------ye ewayBillNo------",current_time)


#####__________eway_deatils__________######
ewbNo = result["ewayBillNo"]
url = f"http://gstsandbox.charteredinfo.com/ewaybillapi/dec/v1.03/ewayapi?action=GetEwayBill&aspid=1683991922&password=Sequelstring@123&gstin=34AACCC1596Q002&username=TaxProEnvPON&authtoken=vYNJHccs08HTWVMUaMZrVfwQ7&ewbNo={ewbNo}"
result = {}
res = requests.get(url, data=json.dumps(result))
result = json.loads(res.text)
# print(result)
print(result["status"],"<-------------ye api ka status hai-----",current_time)

