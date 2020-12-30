#Extend Account from Termination#
$userlist = Get-Content    C:\pathtofile\users.txt

#Grab each user and change the Account Expiration##
foreach ($user in $userlist) {
    Set-ADAccountExpiration -Identity $user -DateTime "01/31/2021"
}