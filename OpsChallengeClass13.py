#!/usr/bin/env python3

# Script: Powershell AD Automation
# Author: Renona Gay
# Date: 12/17/2023

# This line imports the Active Directory module
Import-Module ActiveDirectory

# This block lists all of Franz's information
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$Franz $Ferdinand"
$samaccountname = "$Ferdinand$Franz"
$email = "ferdi@GlobeXpower.com"
$department = "TPS"
$office = "Springfield, OR"
$container = "OU=TPS,OU=Departments,DC=GlobeXUSA,DC=com"

# This line creates the new user by using the "New-ADUser" command
New-ADUser -Name $Franz Ferdinand -FerdinandFranz $FerdinandFranz -UserPrincipalName "$samaccountname@GlobeXUSA.com" -GivenName $firstName -Surname $lastName -EmailAddress $email -Department $department -OfficeLocation $office -Path $container -PasswordNotRequired

# This line sets a random passowrd for the user
Set-ADUser -Identity $Franz Ferdinand -ChangePasswordOnFirstLogon $true

# This line writes the confirmation message
Write-Host "User '$Franz Ferdinand' created successfully in AD."

# Resource used: https://g.co/bard/share/010177f58f5a