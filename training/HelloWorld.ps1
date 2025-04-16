#this is a comment   #cmdlets
Write-Host "Hello World" -NoNewline
Write-Host "again"
#"File created with powershell" | Out-File hello.txt


$Name='Abc'
$Age=100
$Height=6.6
$Present=$true

Write-Host $Name $Age

$Name.GetType()
$Age.GetType()
$Height.GetType()
$Present.GetType()


<#Write-Host
$x=5
$y=10
$x+$y
#>

#Write-Host "length of name" $Name.length

<#$user = Read-Host "Enter a Value: "
Write-Host "HI " $user#>

$area @("chennai","mumbai","delhi")
$area
$area[0]
$area[-1]
$area[1].length

#$area.GetType()


<#Write-Host
$marks=@{"Eng"=80; "Maths"=80; "Sci"=80}
$marks
$marks.Add("Tamil",80)
$marks
$marks.Set_Item("Tamil",100)
$marks
$marks."Maths"
$marks["Maths"]
$marks.Remove("Sci")
$marks
#>

#https://github.com/ab14jain/PowerShell