*** Settings ***
Library    SSHLibrary

*** Variables ***
${HOST}    test.rebex.net
${PORT}    22
${USERNAME}    demo
${PASSWORD}    password

*** Test Cases ***
Connect And Run Command
    Open Connection    ${HOST}
    Set Client Configuration    timeout=5s
    Login    ${USERNAME}    ${PASSWORD}
    ${output}=    Execute Command    ls
    Log    ${output}
    Close Connection