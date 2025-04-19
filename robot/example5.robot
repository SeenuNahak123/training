***Settings***
Library    BuiltIn
Library    Collections

*** Test Cases ***
Add And Remove Items In Dictionary
    ${data}=    Create Dictionary    name=John    age=30
    Log    Original Dictionary: ${data}

    #Add items
    Set To Dictionary    ${data}    name=Elvish    age=32
    Set To Dictionary    ${data}    name=Rocky    age=28   
    Log    After adding: ${data}

    #Remove item
    Remove From Dictionary    ${data}    age
    Log    After removing 'age': ${data}