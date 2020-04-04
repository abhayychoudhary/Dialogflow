def userSays(row):
    userSays = [
        {
            "id": "",
            "data": [
                {
                    "text": row[6],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[7],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[8],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        }, {
            "id": "",
            "data": [
                {
                    "text": row[9],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        }, {
            "id": "",
            "data": [
                {
                    "text": row[10],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[11],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[12],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[13],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[14],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[15],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[16],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[17],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[18],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[19],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        },
        {
            "id": "",
            "data": [
                {
                    "text": row[20],
                    "userDefined": "false"
                }
            ],
            "isTemplate": "false",
            "count": 0,
            "updated": 0
        }
    ]
    return userSays


def noFollowup(row):
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
                        "lang": "en",
                                "condition": "",
                                "speech": row[1]
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": "true",
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return noFollowup


def inputContext(row):
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
                        "lang": "en",
                        "condition": "",
                        "speech": row[1]
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": "true",
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return inputContext


def outputContext(row):
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
                        "lang": "en",
                        "condition": "",
                        "speech": row[1]
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": "true",
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return outputContext




def outputOutputContext(row):
    outputOutputContext = {
        "id": "",
        "name": "upenn.work_return_employee",
        "auto": "true",
        "contexts": [
        row[4]
        ],
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
                "lang": "en",
                "condition": "",
                "speech": row[1]
            }
            ],
            "defaultResponsePlatforms": {},
            "speech": []
        }
        ],
        "priority": 500000,
        "webhookUsed": "true",
        "webhookForSlotFilling": "false",
        "fallbackIntent": "false",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return outputOutputContext
