*** Settings ***
Documentation    A resource file to reuse the keywords and Variables
Library    SeleniumLibrary

*** Variables ***
${user_name}    standard_user
${valid_password}    secret_sauce
${invalid_password}    secret_sauce123

*** keywords ***
Open the browser with saucedemo
    Open Browser    https://www.saucedemo.com/    chrome    