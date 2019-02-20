#this is the shutdown command, giving the user a 5 minute warning
shutdown /s /t 300

#the following creates a message box and collects the user's input/response
Add-Type -AssemblyName PresentationFramework
$ButtonType = [System.Windows.MessageBoxButton]::YesNo
$MessageboxTitle = 'Scheduled Shutdown'
$MessageboxBody = 'Shutdown will occur in 5 minutes. Would you like to cancel the shutdown?'
$MessageIcon = [System.Windows.MessageBoxImage]::Warning
$Result = [System.Windows.MessageBox]::Show($MessageboxBody,$MessageboxTitle,$ButtonType,$MessageIcon)

#this takes the user input and continues or cancels the shutdown
If($Result -eq 'No') {
exit
}
Elseif($Result -eq 'Yes') {
shutdown /a
}
Else {
}

