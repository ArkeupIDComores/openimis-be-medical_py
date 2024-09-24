from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0011_alter'),  # Remplacez par la dépendance correcte
    ]

    operations = [
        migrations.RunSQL(
            # SQL pour créer les vues
            """
            CREATE VIEW [dw].[uvwItemExpenditures]
            AS
                SELECT 
                    SUM(CI.RemuneratedAmount) AS ItemExpenditure,
                    MONTH(ISNULL(C.DateTo, C.DateFrom)) AS MonthTime,
                    DATENAME(QUARTER, ISNULL(C.DateTo, C.DateFrom)) AS QuarterTime,
                    YEAR(ISNULL(C.DateTo, C.DateFrom)) AS YearTime,
                    R.RegionName AS Region,
                    DIns.DistrictName,
                    PR.ProductCode,
                    PR.ProductName,
                    DATEDIFF(YEAR, I.DOB, ISNULL(C.DateTo, C.DateFrom)) AS Age,
                    I.Gender,
                    IType.ItemTypeName,
                    I.ItemCode,
                    I.ItemName,
                    CASE 
                        WHEN DATEDIFF(DAY, C.DateFrom, C.DateTo) > 0 THEN N'I' 
                        ELSE N'O' 
                    END AS ItemCareType,
                    HF.HFLevel,
                    HF.HFCode,
                    HF.HFName,
                    C.VisitType,
                    ICD.ICDCode,
                    ICD.ICDName,
                    DIns.DistrictName AS IDistrictName,
                    W.WardName,
                    V.VillageName,
                    HFD.DistrictName AS HFDistrict,
                    HFR.RegionName AS HFRegion,
                    R.RegionName AS ProdRegion
                FROM 
                    tblClaimItems CI 
                INNER JOIN 
                    tblClaim C ON CI.ClaimID = C.ClaimID
                INNER JOIN 
                    tblProduct PR ON CI.ProdID = PR.ProdID
                INNER JOIN 
                    tblInsuree I ON C.InsureeID = I.InsureeID
                INNER JOIN 
                    tblFamilies F ON I.FamilyID = F.FamilyID
                INNER JOIN 
                    tblVillages V ON V.VillageID = F.LocationId
                INNER JOIN 
                    tblWards W ON W.WardID = V.WardID
                INNER JOIN 
                    tblDistricts DIns ON DIns.DistrictID = W.DistrictID
                INNER JOIN 
                    tblItems I ON CI.ItemID = I.ItemID
                INNER JOIN 
                    tblHF HF ON C.HFID = HF.HfID
                INNER JOIN 
                    tblICDCodes ICD ON C.ICDID = ICD.ICDID
                INNER JOIN 
                    tblDistricts HFD ON HF.LocationId = HFD.DistrictID
                INNER JOIN 
                    tblRegions R ON R.RegionId = DIns.Region
                INNER JOIN 
                    tblRegions HFR ON HFR.RegionId = HFD.Region
                WHERE 
                    CI.ValidityTo IS NULL
                    AND C.ValidityTo IS NULL
                    AND PR.ValidityTo IS NULL
                    AND HF.ValidityTo IS NULL
                    AND HFD.ValidityTo IS NULL
                    AND C.ClaimStatus >= 8
                GROUP BY 
                    MONTH(ISNULL(C.DateTo, C.DateFrom)),
                    DATENAME(QUARTER, ISNULL(C.DateTo, C.DateFrom)),
                    YEAR(ISNULL(C.DateTo, C.DateFrom)),
                    R.RegionName,
                    PR.ProductCode,
                    PR.ProductName,
                    DATEDIFF(YEAR, I.DOB, ISNULL(C.DateTo, C.DateFrom)),
                    I.Gender,
                    IType.ItemTypeName,
                    I.ItemCode,
                    I.ItemName,
                    DATEDIFF(DAY, C.DateFrom, C.DateTo),
                    HF.HFLevel,
                    HF.HFCode,
                    HF.HFName,
                    C.VisitType,
                    ICD.ICDCode,
                    ICD.ICDName,
                    DIns.DistrictName,
                    W.WardName,
                    V.VillageName,
                    HFD.DistrictName,
                    HFR.RegionName;
            
            CREATE VIEW [dw].[uvwServiceExpenditures]
            AS
                SELECT 
                    SUM(CS.RemuneratedAmount) AS ServiceExpenditure,
                    MONTH(ISNULL(C.DateTo, C.DateFrom)) AS MonthTime,
                    DATENAME(QUARTER, ISNULL(C.DateTo, C.DateFrom)) AS QuarterTime,
                    YEAR(ISNULL(C.DateTo, C.DateFrom)) AS YearTime,
                    R.RegionName AS Region,
                    DIns.DistrictName,
                    PR.ProductCode,
                    PR.ProductName,
                    DATEDIFF(YEAR, I.DOB, ISNULL(C.DateTo, C.DateFrom)) AS Age,
                    I.Gender,
                    S.ServType,
                    S.ServCode,
                    S.ServName,
                    CASE 
                        WHEN DATEDIFF(DAY, C.DateFrom, C.DateTo) > 0 THEN N'I' 
                        ELSE N'O' 
                    END AS ServCareType,
                    HF.HFLevel,
                    HF.HFCode,
                    HF.HFName,
                    C.VisitType,
                    ICD.ICDCode,
                    ICD.ICDName,
                    DIns.DistrictName AS IDistrictName,
                    W.WardName,
                    V.VillageName,
                    HFD.DistrictName AS HFDistrict,
                    HFR.RegionName AS HFRegion,
                    R.RegionName AS ProdRegion
                FROM 
                    tblClaimServices CS 
                INNER JOIN 
                    tblClaim C ON CS.ClaimID = C.ClaimID
                INNER JOIN 
                    tblProduct PR ON CS.ProdID = PR.ProdID
                INNER JOIN 
                    tblInsuree I ON C.InsureeID = I.InsureeID
                INNER JOIN 
                    tblFamilies F ON I.FamilyID = F.FamilyID
                INNER JOIN 
                    tblVillages V ON V.VillageID = F.LocationId
                INNER JOIN 
                    tblWards W ON W.WardID = V.WardID
                INNER JOIN 
                    tblDistricts DIns ON DIns.DistrictID = W.DistrictID
                INNER JOIN 
                    tblServices S ON CS.ServID = S.ServID
                INNER JOIN 
                    tblHF HF ON C.HFID = HF.HfID
                INNER JOIN 
                    tblICDCodes ICD ON C.ICDID = ICD.ICDID
                INNER JOIN 
                    tblDistricts HFD ON HF.LocationId = HFD.DistrictID
                INNER JOIN 
                    tblRegions R ON R.RegionId = DIns.Region
                INNER JOIN 
                    tblRegions HFR ON HFR.RegionId = HFD.Region
                WHERE 
                    CS.ValidityTo IS NULL
                    AND C.ValidityTo IS NULL
                    AND PR.ValidityTo IS NULL
                    AND HF.ValidityTo IS NULL
                    AND HFD.ValidityTo IS NULL
                    AND C.ClaimStatus >= 8
                GROUP BY 
                    MONTH(ISNULL(C.DateTo, C.DateFrom)),
                    DATENAME(QUARTER, ISNULL(C.DateTo, C.DateFrom)),
                    YEAR(ISNULL(C.DateTo, C.DateFrom)),
                    R.RegionName,
                    PR.ProductCode,
                    PR.ProductName,
                    DATEDIFF(YEAR, I.DOB, ISNULL(C.DateTo, C.DateFrom)),
                    I.Gender,
                    S.ServType,
                    S.ServCode,
                    S.ServName,
                    DATEDIFF(DAY, C.DateFrom, C.DateTo),
                    HF.HFLevel,
                    HF.HFCode,
                    HF.HFName,
                    C.VisitType,
                    ICD.ICDCode,
                    ICD.ICDName,
                    DIns.DistrictName,
                    W.WardName,
                    V.VillageName,
                    HFD.DistrictName,
                    HFR.RegionName;
            """,
            reverse_sql="""
            DROP VIEW IF EXISTS [dw].[uvwItemExpenditures];
            DROP VIEW IF EXISTS [dw].[uvwServiceExpenditures];
            """
        ),
    ]
