from django.db import models

class Opendatainventory(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    documenttype = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    warehouseregionid = models.CharField(max_length=255)
    warehouseregionname = models.CharField(max_length=255)
    itemgroupid = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    itemtypeid = models.CharField(max_length=255)
    itemtypename = models.CharField(max_length=255)
    measureid = models.CharField(max_length=255)
    measurename = models.CharField(max_length=255)
    itemcategoryid = models.CharField(max_length=255)
    itemcategoryname = models.CharField(max_length=255)
    brandid = models.CharField(max_length=255)
    brandname = models.CharField(max_length=255)
    manufacturerid = models.CharField(max_length=255)
    manufacturername = models.CharField(max_length=255)
    salemeasureid = models.CharField(max_length=255)
    salemeasurename = models.CharField(max_length=255)
    salebasemeasureqty = models.TextField()
    purchasemeasureid = models.CharField(max_length=255)
    purchasemeasurename = models.CharField(max_length=255)
    purchasebasemeasureqty = models.TextField()
    isdebit = models.TextField()
    saleprice = models.TextField()
    unitcost = models.TextField()
    inqty = models.TextField()
    inamt = models.TextField()
    outqty = models.TextField()
    outamt = models.TextField()
    endqty = models.TextField()
    equinqty = models.TextField()
    equoutqty = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataInventory'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatasale(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    weight = models.TextField()
    itemcategoryid = models.CharField(max_length=255)
    itemcategoryname = models.CharField(max_length=255)
    itemsubcategoryid = models.CharField(max_length=255)
    itemsubcategoryname = models.CharField(max_length=255)
    brandid = models.CharField(max_length=255)
    brandname = models.CharField(max_length=255)
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    customerbusinesstypeid = models.CharField(max_length=255)
    customerbusinesstypename = models.CharField(max_length=255)
    customercategoryid = models.CharField(max_length=255)
    customercategoryname = models.CharField(max_length=255)
    customergroupid = models.CharField(max_length=255)
    distributionchannelid = models.CharField(max_length=255)
    distributionchannelname = models.CharField(max_length=255)
    equqty = models.TextField()
    qty = models.TextField()
    price = models.TextField()
    vatamount = models.TextField()
    amountnonvat = models.TextField()
    citytaxamount = models.TextField()
    discountamount = models.TextField()
    payamount = models.TextField()
    unitcost = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataSale'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatarecpay(models.Model):
    rownumber = models.TextField()
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    accountid = models.CharField(max_length=255)
    accountname = models.CharField(max_length=255)
    currencyid = models.TextField()
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    customergroupid = models.CharField(max_length=255)
    isdebit = models.TextField()
    duedate = models.TextField()
    debitamt = models.TextField()
    debitamtfc = models.TextField()
    creditamt = models.TextField()
    creditamtfc = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataRecPay'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatageneralledger(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    documenttypename = models.CharField(max_length=255)
    accountid = models.CharField(max_length=255)
    accountname = models.CharField(max_length=255)
    accounttypename = models.CharField(max_length=255)
    accountgroupid = models.CharField(max_length=255)
    accountgroupname = models.CharField(max_length=255)
    branchid = models.CharField(max_length=255)
    branchname = models.CharField(max_length=255)
    costcenterid = models.CharField(max_length=255)
    costcenter = models.CharField(max_length=255)
    expenseid = models.CharField(max_length=255)
    expensename = models.CharField(max_length=255)
    profitcenterid = models.CharField(max_length=255)
    profitcentername = models.CharField(max_length=255)
    otheraccountsegmentid = models.CharField(max_length=255)
    otheraccountsegment = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    isdebit = models.TextField()
    debitamt = models.TextField()
    debitamtfc = models.TextField()
    creditamt = models.TextField()
    creditamtfc = models.TextField()
    cashflowpropertyid = models.CharField(max_length=255)
    cashflowpropertyname = models.CharField(max_length=255)
    localcashflowpropertyid = models.CharField(max_length=255)
    localcashflowpropertyname = models.CharField(max_length=255)
    s1_id = models.CharField(max_length=255)
    s2_id = models.CharField(max_length=255)
    s3_id = models.CharField(max_length=255)
    s4_id = models.CharField(max_length=255)
    s5_id = models.CharField(max_length=255)
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataGeneralLedger'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataemployee(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    parentname = models.CharField(max_length=255)
    registrynumber = models.CharField(max_length=255)
    departmentid = models.CharField(max_length=255)
    departmentname = models.CharField(max_length=255)
    positionid = models.CharField(max_length=255)
    positionname = models.CharField(max_length=255)
    occupationcategoryid = models.CharField(max_length=255)
    occupationcategoryname = models.CharField(max_length=255)
    insuredtypeid = models.CharField(max_length=255)
    insuredtypename = models.CharField(max_length=255)
    bankid = models.CharField(max_length=255)
    bankname = models.CharField(max_length=255)
    bankaccountid = models.CharField(max_length=255)
    ndshnumber = models.CharField(max_length=255)
    emdnumber = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthdate = models.TextField()
    gender = models.TextField()
    address = models.CharField(max_length=255)
    hiredate = models.TextField()
    basesalary = models.TextField()
    isreclusion = models.TextField()
    reclusiondate = models.TextField()
    d1 = models.TextField()
    d2 = models.TextField()
    d3 = models.TextField()
    d4 = models.TextField()
    d5 = models.TextField()
    d6 = models.TextField()
    d7 = models.TextField()
    d8 = models.TextField()
    d9 = models.TextField()
    d10 = models.TextField()
    d11 = models.TextField()
    d12 = models.TextField()
    d13 = models.TextField()
    d14 = models.TextField()
    d15 = models.TextField()
    d16 = models.TextField()
    d17 = models.TextField()
    d18 = models.TextField()
    d19 = models.TextField()
    d20 = models.TextField()
    d21 = models.TextField()
    d22 = models.TextField()
    d23 = models.TextField()
    d24 = models.TextField()
    d25 = models.TextField()
    d26 = models.TextField()
    d27 = models.TextField()
    d28 = models.TextField()
    d29 = models.TextField()
    d30 = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataEmployee'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatacustomergroup(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    parentpkid = models.TextField()
    sortedorder = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataCustomerGroup'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataasset(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    assettypeid = models.CharField(max_length=255)
    assettypename = models.CharField(max_length=255)
    assetid = models.CharField(max_length=255)
    assetgroupid = models.CharField(max_length=255)
    assetaccountid = models.CharField(max_length=255)
    assetaccountname = models.CharField(max_length=255)
    depraccountid = models.CharField(max_length=255)
    depraccountname = models.CharField(max_length=255)
    assetlocationid = models.CharField(max_length=255)
    assetlocationname = models.CharField(max_length=255)
    employeeid = models.CharField(max_length=255)
    employeename = models.CharField(max_length=255)
    beginuseddate = models.TextField()
    usageyear = models.TextField()
    usagenorm = models.TextField()
    taxusageyear = models.TextField()
    taxusagenorm = models.TextField()
    debitqty = models.TextField()
    creditqty = models.TextField()
    debitamt = models.TextField()
    creditamt = models.TextField()
    debitdepramt = models.TextField()
    creditdepramt = models.TextField()
    debittaxdepramt = models.TextField()
    credittaxdepramt = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataAsset'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatabillofmaterial(models.Model):
    productid = models.CharField(max_length=255)
    productname = models.CharField(max_length=255)
    materialid = models.CharField(max_length=255)
    materialname = models.CharField(max_length=255)
    materialqty = models.TextField()
    materialmeasureid = models.CharField(max_length=255)
    materialmeasurename = models.CharField(max_length=255)
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataBillOfMaterial'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatabrand(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataBrand'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatacustomer(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    registrynumber = models.CharField(max_length=255)
    customergroupid = models.CharField(max_length=255)
    distributionchannelid = models.CharField(max_length=255)
    distributionchannelname = models.CharField(max_length=255)
    pricechannelpkid = models.TextField()
    customerlevel = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    paymenttype = models.CharField(max_length=255)
    paymenttermid = models.CharField(max_length=255)
    paymenttermname = models.CharField(max_length=255)
    customerbehaviorid = models.CharField(max_length=255)
    customerbehaviorname = models.CharField(max_length=255)
    regionid = models.CharField(max_length=255)
    regionname = models.CharField(max_length=255)
    zoneid = models.CharField(max_length=255)
    zonename = models.CharField(max_length=255)
    storeareaid = models.CharField(max_length=255)
    storeareaname = models.CharField(max_length=255)
    subdistributionchannelid = models.CharField(max_length=255)
    subdistributionchannelname = models.CharField(max_length=255)
    customerbusinesstypeid = models.CharField(max_length=255)
    customerbusinesstypename = models.CharField(max_length=255)
    loanlimit = models.TextField()
    activestatus = models.TextField()
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=255)
    modifieddate = models.DateTimeField()
    modifiedby = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataCustomer'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatadistardocument(models.Model):
    documentpkid = models.TextField()
    documentdate = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdesc = models.CharField(max_length=255)
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    debitamt = models.TextField()
    creditamt = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataDistArDocument'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatadistributionchannel(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataDistributionChannel'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataitem(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255,  primary_key=True)
    barcode = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    qtyinpackage = models.TextField()
    baseprice = models.TextField()
    saleprice = models.TextField()
    itemgroupid = models.CharField(max_length=255)
    itemcategoryid = models.CharField(max_length=255)
    itemcategoryname = models.CharField(max_length=255)
    measurename = models.CharField(max_length=255)
    manufacturerid = models.CharField(max_length=255)
    manufacturername = models.CharField(max_length=255)
    itemsubcategoryid = models.CharField(max_length=255)
    itemsubcategoryname = models.CharField(max_length=255)
    brandid = models.CharField(max_length=255)
    brandname = models.CharField(max_length=255)
    itemsizeid = models.CharField(max_length=255)
    itemsizename = models.CharField(max_length=255)
    itemspecialfeatureid = models.CharField(max_length=255)
    itemspecialfeaturename = models.CharField(max_length=255)
    itemcolorid = models.CharField(max_length=255)
    itemcolorname = models.CharField(max_length=255)
    itemgenderid = models.CharField(max_length=255)
    itemgendername = models.CharField(max_length=255)
    shelfid = models.CharField(max_length=255)
    shelfname = models.CharField(max_length=255)
    convertitemid = models.CharField(max_length=255)
    convertitemname = models.CharField(max_length=255)
    searchvalue = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    volume = models.TextField()
    weight = models.TextField()
    activestatus = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataItem'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataseller(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    sellerteamid = models.CharField(max_length=255)
    sellerteamname = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=255)
    receivableaccountid = models.CharField(max_length=255)
    receivableaccountname = models.CharField(max_length=255)
    payableaccountid = models.CharField(max_length=255)
    payableaccountname = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataSeller'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatawarehouse(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    warehouseregionid = models.CharField(max_length=255)
    warehouseregionname = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataWarehouse'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataitemprice(models.Model):
    pricedate = models.TextField()
    itempkid = models.TextField()
    customerpkid = models.TextField()
    pricechannelpkid = models.TextField()
    measurepkid = models.TextField()
    purchaseprice = models.TextField()
    baseprice = models.TextField()
    discountpercent = models.TextField()
    price = models.TextField()
    wholeprice = models.TextField()
    wholeqty = models.TextField()
    wholepriceactivestatus = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataItemPrice'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataitempricechannel(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    parentpkid = models.TextField()
    copypkid = models.TextField()
    factor = models.TextField()
    smartorderchannelid = models.CharField(max_length=255)
    notusediscount = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataItemPriceChannel'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataaccount(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataAccount'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatauser(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataUser'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatapurchase(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    vendorid = models.CharField(max_length=255)
    vendorname = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    buyerid = models.CharField(max_length=255)
    buyername = models.CharField(max_length=255)
    paymentaccountid = models.CharField(max_length=255)
    paymentaccountname = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    measureid = models.CharField(max_length=255)
    measurename = models.CharField(max_length=255)
    equqty = models.TextField()
    qty = models.TextField()
    unitcost = models.TextField()
    saleprice = models.TextField()
    price = models.TextField()
    amount = models.TextField()
    vatamount = models.TextField()
    amountnonvat = models.TextField()
    discountamount = models.TextField()
    profitamount = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataPurchase'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatalandedcost(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    vendorid = models.CharField(max_length=255)
    vendorname = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    contractid = models.CharField(max_length=255)
    contractname = models.CharField(max_length=255)
    vendoraccountid = models.CharField(max_length=255)
    vendoraccountname = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    measureid = models.CharField(max_length=255)
    measurename = models.CharField(max_length=255)
    currencyid = models.CharField(max_length=255)
    rate = models.TextField()
    equqty = models.TextField()
    qty = models.TextField()
    unitcost = models.TextField()
    saleprice = models.TextField()
    price = models.TextField()
    itemamount = models.TextField()
    itemamountfc = models.TextField()
    amount = models.TextField()
    vatamount = models.TextField()
    amountnonvat = models.TextField()
    customamount = models.TextField()
    otherexpenseamount = models.TextField()
    totalexpenseamount = models.TextField()
    ratediffamount = models.TextField()
    profitamount = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataLandedCost'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatainventorysubline(models.Model):
    documentpkid = models.TextField()
    documentdate = models.TextField()
    documenttype = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    towarehouseid = models.CharField(max_length=255)
    towarehousename = models.CharField(max_length=255)
    measureid = models.CharField(max_length=255)
    measurename = models.CharField(max_length=255)
    isdebit = models.TextField()
    inqty = models.TextField()
    outqty = models.TextField()
    expirationtype = models.CharField(max_length=255)
    batchnumber = models.CharField(max_length=255)
    serialnumber = models.CharField(max_length=255)
    expiredate = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataInventorySubLine'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatasalerefund(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    weight = models.TextField()
    itemcategoryid = models.CharField(max_length=255)
    itemcategoryname = models.CharField(max_length=255)
    itemsubcategoryid = models.CharField(max_length=255)
    itemsubcategoryname = models.CharField(max_length=255)
    brandid = models.CharField(max_length=255)
    brandname = models.CharField(max_length=255)
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    customerbusinesstypeid = models.CharField(max_length=255)
    customerbusinesstypename = models.CharField(max_length=255)
    customercategoryid = models.CharField(max_length=255)
    customercategoryname = models.CharField(max_length=255)
    customergroupid = models.CharField(max_length=255)
    distributionchannelid = models.CharField(max_length=255)
    distributionchannelname = models.CharField(max_length=255)
    qty = models.TextField()
    price = models.TextField()
    vatamount = models.TextField()
    amountnonvat = models.TextField()
    citytaxamount = models.TextField()
    discountamount = models.TextField()
    payamount = models.TextField()
    unitcost = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataSaleRefund'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatasupply(models.Model):
    documentpkid = models.TextField()
    documentnumber = models.CharField(max_length=255)
    documentdate = models.TextField()
    documentdesc = models.CharField(max_length=255)
    documenttype = models.CharField(max_length=255)
    supplyitemid = models.CharField(max_length=255)
    supplyitemname = models.CharField(max_length=255)
    itemid = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    accountid = models.CharField(max_length=255)
    expenseaccountid = models.CharField(max_length=255)
    costaccountid = models.CharField(max_length=255)
    accounttype = models.CharField(max_length=255)
    journaltype = models.TextField()
    warehouseid = models.CharField(max_length=255)
    employeeid = models.CharField(max_length=255)
    employeename = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    basemeasureid = models.CharField(max_length=255)
    basemeasureqty = models.TextField()
    measureid = models.CharField(max_length=255)
    isdebit = models.TextField()
    unitcost = models.TextField()
    debitqty = models.TextField()
    creditqty = models.TextField()
    debitamt = models.TextField()
    creditamt = models.TextField()
    debitexpenseamt = models.TextField()
    creditexpenseamt = models.TextField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataSupply'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataaccountbudget(models.Model):
    rownumber = models.TextField()
    budgettype = models.CharField(max_length=255)
    budgetyear = models.TextField()
    accountpkid = models.TextField()
    yearamount = models.TextField()
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    jan = models.TextField()
    feb = models.TextField()
    mar = models.TextField()
    apr = models.TextField()
    may = models.TextField()
    jun = models.TextField()
    jul = models.TextField()
    aug = models.TextField()
    sep = models.TextField()
    oct = models.TextField()
    nov = models.TextField()
    dec = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataAccountBudget'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatacashprojectbudget(models.Model):
    projectyear = models.IntegerField()
    cashprojectpkid = models.TextField()
    cashprojectjobpkid = models.TextField()
    cashprojectjobid = models.CharField(max_length=255)
    cashprojectjobname = models.CharField(max_length=255)
    cashprojectjobtype = models.CharField(max_length=255)
    amount = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataCashProjectBudget'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatapurchasemonthlybudget(models.Model):
    warehousepkid = models.TextField()
    budgetyear = models.TextField()
    budgetmonth = models.TextField()
    duedate = models.TextField()
    itempkid = models.TextField()
    price = models.IntegerField()
    qty = models.TextField()
    amount = models.TextField()
    percent = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataPurchaseMonthlyBudget'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatareport(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataReport'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatareportbudget(models.Model):
    budgettype = models.CharField(max_length=255)
    budgetyear = models.TextField()
    reportpkid = models.TextField()
    propertypkid = models.TextField()
    yearamount = models.TextField()
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    jan = models.TextField()
    feb = models.TextField()
    mar = models.TextField()
    apr = models.TextField()
    may = models.TextField()
    jun = models.TextField()
    jul = models.TextField()
    aug = models.TextField()
    sep = models.TextField()
    oct = models.TextField()
    nov = models.TextField()
    dec = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataReportBudget'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatareportproperty(models.Model):
    pkid = models.TextField()
    reportpkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    nameeng = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataReportProperty'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataitemcategory(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataItemCategory'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatasalesbudget(models.Model):
    rownumber = models.TextField()
    budgetyear = models.TextField()
    budgetmonth = models.TextField()
    budgetamount = models.TextField()
    budgetquantity = models.TextField()
    sellerpkid = models.TextField()
    brandpkid = models.TextField()
    itempkid = models.TextField()
    customerpkid = models.TextField()
    warehousepkid = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataSalesBudget'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatacurrencyrate(models.Model):
    currencyid = models.CharField(max_length=255)
    date = models.TextField()
    rate = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataCurrencyRate'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatadistributor(models.Model):
    pkid = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    disttype = models.CharField(max_length=255)
    isactive = models.TextField()
    warehouseid = models.CharField(max_length=255)
    warehousename = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customename = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataDistributor'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataroute(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataRoute'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataroutecustomer(models.Model):
    routeid = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    customergroupid = models.CharField(max_length=255)
    distributionchannelid = models.CharField(max_length=255)
    distributionchannelname = models.CharField(max_length=255)
    latitude = models.TextField()
    longitude = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataRouteCustomer'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendataroutepoint(models.Model):
    routeid = models.CharField(max_length=255)
    latitude = models.TextField()
    longitude = models.TextField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataRoutePoint'  # MSSQL дахь нэртэй тааруулж өгнө

class Opendatasellercustomer(models.Model):
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    routeid = models.CharField(max_length=255)
    routename = models.CharField(max_length=255)
    customerid = models.CharField(max_length=255)
    customername = models.CharField(max_length=255)
    mondays = models.TextField()
    tuesdays = models.TextField()
    wednesdays = models.TextField()
    thursdays = models.TextField()
    fridays = models.TextField()
    saturdays = models.TextField()
    sundays = models.TextField()
    frequencytype = models.CharField(max_length=255)
    visitqty = models.IntegerField()
    class Meta:
        managed = False  # View учраас Django удирдахгүй
        db_table = 'OpenDataSellerCustomer'  # MSSQL дахь нэртэй тааруулж өгнө

