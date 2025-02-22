expected_output = {
    "vrfs":{
        "MCAST_VRF_A":{
            "groups_count":4,
            "interface":{
                "Vlan20":{
                    "group":{
                        "ff04:230:11:1::1":{
                            "type":"d",
                            "expire":"00:03:50",
                            "up_time":"23:20:22",
                            "last_reporter":"fe80::10:22:1:10"
                        },
                        "ff3e:232:11:1::1":{
                            "source":{
                                "10:11:1::10":{
                                    "type":"d",
                                    "expire":"00:03:50",
                                    "up_time":"23:20:22",
                                    "last_reporter":"fe80::10:22:1:20"
                                }
                            }
                        }
                    }
                },
                "Vlan2":{
                    "group":{
                        "ff04:230:11:1::1":{
                            "type":"d",
                            "expire":"00:02:36",
                            "up_time":"23:20:22",
                            "last_reporter":"fe80::10:23:4:30"
                        },
                        "ff3e:232:11:1::1":{
                            "source":{
                                "10:11:1::10":{
                                    "type":"d",
                                    "expire":"00:02:36",
                                    "up_time":"23:20:22",
                                    "last_reporter":"fe80::10:23:4:40"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}