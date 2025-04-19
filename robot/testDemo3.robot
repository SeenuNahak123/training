*** Settings ***
Documentation    To Validate a login From
Library    SeleniumLibrary
Test Setup    Open the browser with saucedemo
Test Teardown    Close Browser
Resource    resource.robot


*** Test Cases ***
Validate Cards Display in shopping page
    Fill The Login Form    ${user_name}    ${valid_password}
    wait till a element is Visible    xpath://*[@id="shopping_cart_container"]/a
    Verify Card titles in the shop page
    Select the Card    Sauce Labs Fleece Jacket

*** keywords ***
Fill the login Form
    [Arguments]    ${username}    ${password}
    Input Text    user-name   ${username}
    Input Password    password   ${password}
    Click Button    login-button


wait till a element is visible
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}


Verify Card titles in the shop page
    @{expectedlist}=    Create List
    ...    Sauce Labs Backpack
    ...    Sauce Labs Bike Light
    ...    Sauce Labs Bolt T-Shirt
    ...    Sauce Labs Fleece Jacket
    ...    Sauce Labs Onesie
    ...    Test.allTheThings() T-Shirt (Red)
    ${elements}=    Get WebElements    css:.inventory_item_name
    FOR    ${element}    IN    @{elements}
        ${text}=    Get Text    ${element}
        Should Contain    ${expectedlist}    ${text}
        Log    Validate Card Title: ${text}
    END


Select the Card    
        [Arguments]    ${card_name}
        ${elements}=    Get WebElements    css:.inventory_item_name
        ${index}=    Set Variable    
        FOR    ${element}    IN    @{elements}
            ${text}=    Get Text    ${element}
            Exit For Loop If    '${card_name}' == '${text}'
                ${index}=    Evaluate    ${index} + 1
        END
        Log    ${index}
        Click Button    xpath:(//*[@class='pricebar'])[${index}]/button
        Sleep    3