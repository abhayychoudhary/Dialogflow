import json

def userSays(row):
        userSays = []
        for i in row[10:]:
            if(i):
                userSays.append({"id": "","data": [{"text": i,"userDefined": "false"}],"isTemplate": "false","count": 0,"updated": 0})
        return userSays


def noFollowup(row):
    def webhook(row):
        if(row=="" or row.lower()=="false"):
            return False
        else:
            return True
    noFollowup = {
        "id": "",
        "name": row[0],
        "auto": "true",
        "contexts": [],
        "responses": [
            {
                "resetContexts": "false",
                "affectedContexts": [],
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": "hi",
                                "condition": "",
                                "speech": row[1]
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return noFollowup


def inputContext(row):
    def webhook(row):
        if(row=="" or row.lower()=="false"):
            return False
        else:
            return True
    inputContext = {
        "id": "",
        "name": row[0],
        "auto": "true",
        "contexts": [],
        "responses": [
            {
                "resetContexts": "false",
                "affectedContexts": [
                    {
                        "name": row[3],
                        "parameters": {},
                        "lifespan": 2
                    }
                ],
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": "hi",
                        "condition": "",
                        "speech": row[1]
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return inputContext


def outputContext(row):
    def webhook(row):
        if(row=="" or row.lower()=="false"):
            return False
        else:
            return True
    outputContext = {
        "id": "",
        "name": row[0],
        "auto": "true",
        "contexts": [
            row[4]
        ],
        "responses": [
            {
                "resetContexts": "false",
                "affectedContexts": [],
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": "hi",
                        "condition": "",
                        "speech": row[1]
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return outputContext


def outputOutputContext(row):
    def webhook(row):
        if(row=="" or row.lower()=="false"):
            return False
        else:
            return True

    def chip(row):
        chip = []
        for i in row.split("/"):
            chip.append({"text": i})
        return chip

    def chipgoogle(row):
        chipgoogle = []
        for i in row.split("/"):
            chipgoogle.append({"title": i})
        return chipgoogle

    def outputnewcontext(row):
        outputcontextadd = []
        for i in row.split("/"):
            outputcontextadd.append(
                {"name": i.split("=")[0], "parameters": {}, "lifespan": i.split("=")[1]})
        return outputcontextadd

    def inputnewcontext(row):
        inputnewcontext = []
        for i in row.split("/"):
            inputnewcontext.append(i)
        return inputnewcontext

    data = chip(row[6])[0].get("text", "")

    if data:
        outputOutputContext = {
            "id": row[7] or "",
            "name": row[0],
            "auto": "true",
            "contexts": inputnewcontext(row[4]),
            "responses": [
                {
                    "resetContexts": "false",
                    "affectedContexts": outputnewcontext(row[3]),
                    "parameters": [],
                    "messages": [
                        {
                            "type": "suggestion_chips",
                            "platform": "google",
                            "lang": "hi",
                            "condition": "",
                            "suggestions": chipgoogle(row[6])
                        },
                        {
                            "type": 0,
                            "lang": "hi",
                            "condition": "",
                            "speech": row[1]
                        },
                        {
                            "type": 4,
                            "lang": "hi",
                            "condition": "",
                            "payload": {
                                "richContent": [
                                    [
                                        {
                                            "type": "chips",
                                            "options": chip(row[6])
                                        }
                                    ]
                                ]
                            }
                        }

                    ],
                    "defaultResponsePlatforms": {
                        "google": "true"
                    },
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": webhook(row[8]),
            "webhookForSlotFilling": "false",
            "fallbackIntent": "false",
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
    else:
        outputOutputContext = {
            "id": row[7] or "",
            "name": row[0],
            "auto": "true",
            "contexts": inputnewcontext(row[4]),
            "responses": [
                {
                    "resetContexts": "false",
                    "affectedContexts": outputnewcontext(row[3]),
                    "parameters": [],
                    "messages": [
                        {
                            "type": 0,
                            "lang": "hi",
                            "condition": "",
                            "speech": row[1]
                        }

                    ],
                    "defaultResponsePlatforms": {
                        "google": "true"
                    },
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": webhook(row[8]),
            "webhookForSlotFilling": "false",
            "fallbackIntent": "false",
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }

    return outputOutputContext


def defaultcontext(row):
    def webhook(row):
        if(row=="" or row.lower()=="false"):
            return False
        else:
            return True

    def chip(row):
        chip = []
        for i in row.split("/"):
            chip.append({"text": i})
        return chip

    def chipgoogle(row):
        chipgoogle = []
        for i in row.split("/"):
            chipgoogle.append({"title": i})
        return chipgoogle

    def inputnewcontext(row):
        inputnewcontext = []
        for i in row.split("/"):
            inputnewcontext.append(i)
        return inputnewcontext

    defaultcontext = {
        "id": "",
        "parentId": row[7] or "",
        "rootParentId": row[7] or "",
        "name": row[0],
        "auto": "false",
        "contexts": inputnewcontext(row[4]),
        "responses": [
            {
                "resetContexts": "false",
                "action": "",
                "affectedContexts": [],
                "parameters": [],
                "messages": [
                    # {
                    #     "type": "suggestion_chips",
                    #     "platform": "google",
                    #     "lang": "hi",
                    #     "condition": "",
                    #     "suggestions": chipgoogle(row[6])
                    # },
                    {
                        "type": 0,
                        "lang": "hi",
                        "condition": "",
                        "speech": row[1]
                    },
                    # {
                    #     "type": 4,
                    #     "lang": "hi",
                    #     "condition": "",
                    #     "payload": {
                    #         "richContent": [
                    #             [
                    #                 {
                    #                     "type": "chips",
                    #                     "options": chip(row[6])
                    #                 }
                    #             ]
                    #         ]
                    #     }
                    # }
                ],
                "defaultResponsePlatforms": {
                        "google": "true"
                    },
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": "false",
        "fallbackIntent": "true",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return defaultcontext
