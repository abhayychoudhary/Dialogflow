import json


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

    data = chip(row[22])[0].get("text", "")

    if data:
        outputOutputContext = {
            "id": row[23] or "",
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
                            "lang": "en",
                            "condition": "",
                            "suggestions": chipgoogle(row[22])
                        },
                        {
                            "type": 0,
                            "lang": "en",
                            "condition": "",
                            "speech": row[1]
                        },
                        {
                            "type": 4,
                            "lang": "en",
                            "condition": "",
                            "payload": {
                                "richContent": [
                                    [
                                        {
                                            "type": "chips",
                                            "options": chip(row[22])
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
            "webhookUsed": "false",
            "webhookForSlotFilling": "false",
            "fallbackIntent": "false",
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
    else:
        outputOutputContext = {
            "id": row[23] or "",
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
                            "lang": "en",
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
            "webhookUsed": "false",
            "webhookForSlotFilling": "false",
            "fallbackIntent": "false",
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }

    return outputOutputContext


def defaultcontext(row):
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
        "parentId": row[23] or "",
        "rootParentId": row[23] or "",
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
                    {
                        "type": "suggestion_chips",
                        "platform": "google",
                        "lang": "en",
                        "condition": "",
                        "suggestions": chipgoogle(row[22])
                    },
                    {
                        "type": 0,
                        "lang": "en",
                        "condition": "",
                        "speech": row[1]
                    },
                    {
                        "type": 4,
                        "lang": "en",
                        "condition": "",
                        "payload": {
                            "richContent": [
                                [
                                    {
                                        "type": "chips",
                                        "options": chip(row[22])
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
        "webhookUsed": "false",
        "webhookForSlotFilling": "false",
        "fallbackIntent": "true",
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return defaultcontext
