import base64
myscript = b'aW1wb3J0IGJhc2U2NApteXNjcmlwdD1iJ2FXMXdiM0owSUdKaGMyVTJOQXB0ZVhOamNtbHdkRDFpSjFnd1RUbEtlVEZ3WW0xWmJrTnNPVU5RVTJSd1ltMVpia05zT1VKUVUyUXlXVmQ0Y0ZwRFkwdGhWekYzWWpOS01FbElTbWhpYlZKMllsTjRkV1JYTVhkbFUwSm9ZM2xDZFdORGVERmtSMnh6WTNkd2FtSkhSbnBqZVVKUVkwaENkbUp0Vm5Wa1JURndZbTFzZEZsWWFGRmlSMFkxV2xoSmIyUllVbkJpU0UxMVZVZDRhR1ZYVm5sTFZHOUxRMWRTYkZwcFFtWllNbXgxWVZoU1psaDVhRUpNUjFKc1kwaFNiMUJVU1hCUGFXUmpZbWxCWjBsRFFXZEpRMEZuVDI1Q2FHTnRSblJKUjFKc1kwaFNiMDlwUW5sYVYwNHhZMjVPY0dJeU5HZGFSMVozWkVkb1kySnNlSFZKUTBGblNVTkJaMGxEUW5SWldHaHJZVmhPTUU5cFFtcGlNalY2WVZkU2JHTnBRblppYlhnMVNVaENkbU15YkRCaFZ6bDFZM2xDTTJGWVVtOUpSekZvWlVkU2NHTXpVV2RpVjBZMFlWY3hhR0pEUW1oaVIzaDJaREpXYTBsSFVuQmpNMUpvWW0xT2JFbEhXbmxpTWpCblpFZEdjbHBYTkdkalJ6bDZZVmhTY0dJeU5XTmlhVUZuU1VOQlowbERRV2RLZW5SNlpGaENiR05wWjNCTWJEbG1ZVmMxY0dSR09XWkxRMnMzVVZNMWExcFlRakJoUkRGcldsaENNR0ZFZEVKTWJURm9aVWRTY0dNelVUbE5hblJDVEc1T01GbFlVbXhZTW5Sc1kyMDFiR0pFTVU5aU1qVnNRMmRzYTFwWFdXZGliVlkwWkVZNWRHSXpXbXhMUlVWeldXMDVhR050VVhCUFoyOUtRMU5rWTJKcFFXZEpRMEZuU1VOQlowOXVRbWhqYlVaMFNVZEtkbGxZU210UGFVSlZZVmRPVlZsWFRsVmlNbFZuV1cwNWFHTnRVV2RaV0UxblRXdFJaMkp0VW1oamJrcG9aVk0xWTJKcFFXZEpRMEZuU1VOQlowOXVTbXhrU0ZaNVltcHZaMk50T1ROTVEwSnFZakozWjB4VFFuZGlNMDV3WkVkc2RtSnBRblphYVVJd1lVZFZaMkp0VmpSa1EwSjBZak5hYkVsSGJIVkpSMHAyV1ZoS2EwOXBRbWxpTWtaNVdrWjBlV0l6WkdSWE1rNTJZa1l4WTJKcFFXZEpRMEZuU1VOQlowcDZkRU5RVjBwMldWaEthMDh3UlhWak0xSm9aRWRXWm1FeVZubGliVlp6VUZjMWQweHRPWFZhV0UxdlpGaFNjR0pJVFhWV01HeFBXREZPVlZGV1VrWllNSGhHVkdsNGEyUkliSGRhVkRGRFRHMVNNR1ZZUW14TFZIUkdURVZOYzFKRU1VSk1iVEZ3WW0xc2RGbFlaMjlhUjFaM1pFZG5PVkZUTld0YVdFSXdZVU40YVdJeVJubGFSREZEVEVkT01XTnVTbXhpYmxKbVlsYzVNbHBXT1hSWldFcHlXbGhKT1ZGVE5VNVJWa3BNVWxaSmNFOHpRbmxoVnpVd1MwZFphV1Y1WkU1UlZtZHVZVmRaWjFGVE5VNVJWa3BNVWxaSk9WQlVSV2RhVjNoNldsTmtUbE5WTkc1bVUwSjZXVEk1ZVZwVWIyZGxNRlk1U1dsclMwTlJiSEJhYVVKRVVGUXhSVkJVTUhSTlZHOUxRMUZyU21ReWFIQmlSMVZuVmtoS01WcFViMHREVVd0S1ExVk5PV050Um5WYVJ6bDBURzFPYjJJeWJHcGFVMmh6WVZoT01FdElTbWhpYldSc1MwVkpkV015YUdoalIxWmlUVVl3Y0V0VGF6ZFNSREY1V1ZjMWEySXlNSFZaTW1oMllWZE9iRXRIZUhCak0xRnZZMjFHZFZveVZXOVJhVFY2WVVkR2QxcFdjM2hZVTJ0d1MxRnZTa05SYTBwaFYxbG5VV3gwUkZoV2RFVllWREE1VFVSd2FXTnRWbWhoZDI5S1ExaEtiR1JJVm5saWFVSkVURVZSUzBOWFVteGFhVUptV2pKV01GZ3lVbkJqYlZacVpFZHNkbUpzT1hwa1IwWXdXbGhOYjFScGVHbGlNa1o1V2tONGVXSXpaSEJNUjA1MllrZHJjRTluYjBwRFZWVTVXVEk1YzJGVWRFVlFXRXAyWkRKck4xRnFNV2xpTWtaNVdrUjBRbEJXZEdSUE1FMDVWekV3TjFKcU1YUlpXR2R2VWxNeE1XUkhiSE5qZVRWWVUxVTFabFV4VWtKV1JWWm1WRVZXVDB0NlJYTk5RMnMzVTJveFJrc3pWakJoVjNoNlRHeGtTbFJzT1ZSV1JVWlZVbFk1VFZKVk5EZFJVelZvWTBoQ2JHSnRVVzlSYkhSRlRFVlpObE5zTUhCUE1FMTFXVmhDZDFwWE5XdExSVlYwVW1sck4xSnFNWFJaV0dkdlVrTXhNV1JIYkhOamVUVllVMVUxWmxVeFVrSldSVlptVkVWV1QwdDZSWE5OUTJzM1Uyb3hSVXN6VmpCaFYzaDZUR3hrU2xSc09WUldSVVpWVWxZNVRWSlZORGRSVXpWb1kwaENiR0p0VVc5UmJIUjBXVmhuYjFKcGQzZExWSEJMVEVWV1pFdFVkRVJNYlVaM1kwZFdkVnBEYUVWTVZWbHdUekJ6T1ZjeE1EZFVSREZpV0ZGdlNrTlhXblpqYVVKSVNVZHNkVWxJU21oaWJXUnNTME14TVdSSGJITmplVFZZVTFVMVpsVXhVa0pXUlZabVZFVldUMHQ2UlhOa1dGSndZa2hOZFZZd2JFOVlNVTVWVVZaU1JsZ3dlRVpVYVdzMlEyZHJTa05YYkcxSlJXTTVVRlJCTmxGNU5XaGpTRUpzWW0xUmIySkhWblZMUlhOd1MxUjBSRXh0Um5kalIxWjFXa05vYzFwWE5HOVVRMnR3UTJkclNrTlZaemxTUTNSSVR6QnJPVkpUZEVoRFoydEtRMWRzYlVsRVFUaFFWV2M0VVdrMWVtRkhSbmRhVm5OM1dGZEdkVnBEUVhkUVJERktVRVZKZFdNeWFHaGpSMVppVFZZd05sTjVOV2hqU0VKc1ltMVJiMUZzZEVsTVJXeGtTMUZ2U2tOUmJFbFFWVkZ5VW5wMFNsQlZWWFJTZDI5S1ExRnNjRnBwUVhkUVJERkpVRVZKZFdNeWFHaGpSMVppVFVZeGFHSnRVV2ROUkhjNVUxUjRRMHh1VG05WldFSnNWM3BHWkU5cmQzVlpXRUozV2xjMWEwdEZTbUpUUTNoS1dGTnJTME5SYkVKTWJVWjNZMGRXZFZwRGFIVmpRelZvWXpKR2VXTnRSalZMUlhOd1MxUjBRa3h0Um5kalIxWjFXa05vZFdORE5XaGpNa1o1WTIxR05VdEZkM0JMVkhST1VGWjBRMGxIV25aamFVSkRTVWRzZFVsSVNtaGliV1JzUzBkNGJHSnBhRUpMVTJ4d1dtbENRbGN3U21STWJrNXdaVzFWSzFCWVZqQmhWM2g2VEd4a1NsUnNPVlJXUlVaVlVsWTVUVkpWTldSUE1FVTVWekJHWWxGc01XMWlNMGxuVVdsQ2NHSnBRazVZVkhSRVVGWjBSRmN3Um1SYWJUbDVTVVZGWjJGWE5HZFVWakEzWTIxV01HUllTblZKUlVWelVYZHZTbHBIVm0xSlIxWXlXVmQ0Wm1KWE9USmFVMmhEVEVoT01GbFlVbXhqZVdzMlEyZHJTbHB0T1hsSlJVMW5ZVmMwWjJNelVtaGtSMVo2VDJkdlNrTlJiRUpRVnpWM1RHMU9kbUp1V25aaVNGcHNTMFZOYzFGcE5YcGtSMFl3V2xZNWNscFlTblZhVjNkeldEQkZjRU5uYTBwRFYyeHRTVWMxZDB4dE1XaGxRMmhDUzFRd09XUllVbkJpU0UxMVZqQnNUMWd4VGxWUlZsSkdXREI0UmxScWNIbGFXRkl4WTIwMFoxcHRlSFpaV0ZGdldEQkpjRU5uYTBwRFYyeHRTVWMxZDB4dE1YQmlhV2hDUzFRd09VeFlWakJoVjNoNlRHeGtTbFJzT1ZSV1JVWlZVbFk1VFZKVk5EWmpiVll3WkZoS2RVbEhXbk5pTWtZd1MwWTVSRXRSYjBwRFdFcHNaRWhXZVdKcFFrOWlNalZzUTJkc2ExcFhXV2RoUjFZeFkyMXNlbVJIYkdwWU1sWXlXVmQ0TVZsWVVuQmlNalZtWWxjNU1scFdPV3RoVjFwdFMwVk5jMk16VW1oa1IxWjZURWhPTUZsWVVteFlNakYyWkcxV2VrdFViMHREVVd4RlVGUkJTME5SYkcxaU0wbG5TMFZGYzFGcGEyZGhWelJuWlcxc2QwdElUakJaV0ZKc1kzbDRlbVJIUmpCYVZqbDBZak5hYkdONWF6WlNWREZDVnpCS1pFOHdSbUpSYkRBNVRVUjBSMUJWVFhWWU1taHNaRmhLY0dNelVuQlpNVGxzWkcxR2MxZ3pUakJaV0ZKc1MwVkZjRTh3Um1KUmJEQTVVbFIwU0ZCVlRYVllNbWhzWkZoS2NHTXpVbkJaTVRsc1pHMUdjMWd6VGpCWldGSnNTMFZGY0U4d1VYSlFWV04wVW1kdlNrTllTbXhrU0ZaNVltbENSVU5uYkd0YVYxbG5XREpvYkdSWVNuQmpNMUp3V1RFNWJHUnRSbk5ZTTA0d1dWaFNiRXRGV1hOak0xSm9aRWRWY0U5bmIwcERWV001WXpOU2FHUkhWVGRSYWpGMVkwTTFhbUl5TlRKaU1uZ3lXbE5vU0V4RldYVmpNMUpvWkVkV1ptRXlWbmxpYlZaelRFWTVRa3RVZEVSUVZ6VjNURzFPZG1KdVduWmlTRnBzUzBWak9WQlRNSGhNUlZsMVl6TlNhR1JIVm1aaE1sWjVZbTFXYzB4R09VSkxWSFJGVUZWSmNsRjZkRVJNUlZFNVVYbHZiMUpFTURsTlEydHpVa052YjFGNk1EbE5RMnMzVWxReGRXTkROWHBrVnpCdlVrTnZjVTE1TVVSTGFXOTZTMUZ2U2tOWGJHMUpSM2hzWW1sb1EwdFVORGxOYW05TFExRnJTbE5FTVhWalF6VjBXVmhuYjFGcGF6ZFRWREYxWTBNMWRHRlhORzlSYVd0TFExRnJTbUZYV1dkVFJEQTVaRmhTY0dKSVRYVldNR3hQV0RGT1ZWRldVa1pZTUhoR1ZHa3dlRTluYjBwRFVXdEtVVlF3YjFGcU1EbFRRMnQxV1ZoT01HVllRbXhMUjJ4MVpFTnJOMUZVTVhWalF6VnFZakkxTW1JeWVESmFVMmhDVEVjMWQweHRPWFZhV0UxdlRXbDRhMlJJYkhkYVZERndZbTVSY0V4R09VSkxVVzlLUTFGclNtRlhXV2ROYVVKd1ltbENRazlyVlhKUVZFVjNTMmx2TlVObmEwcERWMnh0U1VWck9WQlRNVEZrUjJ4elkzazFXRk5WTldaVk1WSkNWa1ZXWmxSRlZrOUxla1UyUTJkclNrTlJiRUpRVTJoRFVGUXhTa3RUTldoak0xSTFZMGRWYjJGWE5UQkxWSFJDVUZjMWQweHRUblppYmxwMllraGFiRXRGUlhOaWJrRjFZakkxYkdONVozbE1SMUl3WlZoQ2JGQlhiSFZrUTJ0eldEQkZjRU5uYTBwRFVXeHdXbWxCZVVsSGJIVkpSVVUyVWxNd09VMVVRWEZMYW10TFExRnNlVnBZVWpGamJUUm5VbEZ2U2xwSFZtMUpSMlJzWkVZNWQySXpUbkJrUjJ4MlltNU5iMUZUZUdsaU1rWjVXa05yTmtObmEwcFJlakZwWWpKR2VWcEVNRGxOUkhSRFVGZzBaMUY2ZEVkUVZ6VjNURzFHZVZvelpHOWFXRXBzUzBWSmNFTm5hMHBhYlRsNVNVTm9SVXhGVlhCSlIyeDFTVVZaTmxGc2RIUlpXR2R2VWtNeFFreHRNV2hsUjFKd1l6TlJjMDFEYXpaU1EzUkNURzB4YUdWSFVuQmpNMUZ5VFZONGRGbFlaMjlTVXpGQ1RHMHhhR1ZIVW5Cak0xRnpUVU5yTmxKVGRFSk1iVEZvWlVkU2NHTXpVWEpOVmpBNVZraEtNVnBSYjBwRFZXTTVVWGx3UTA4elNteGtTRlo1WW1sQ2RXTkROV2hqYldRellVZFdlVnBUYUVoTFVXOUtXa2RXYlVsSVNteFpNVGwwWVZjMWNHSlhSalJMUlZWeldrZFdkMlJIWjNOWmJUbG9ZMjFSYzFrelZubGpiVloxWkVZNWVsa3lPWGxhVTNocVpGaEtlVnBYTlRCWU1qRjJaRzFXWm1KWFJubGhNbFo1VEVjeGRtUnRWbVpqYlRrelRFY3hkbVJ0Vm1aWk1qbHpURWRHYzJOSGFHaE1SMHBzWkVkRmNFOW5iMHBEVlc4NVdrZFdkMlJIWnpkVFZERnFaRmhLZVZwWE5UQllNMDVxWWpOS2JFOHdaemxaTTFaNVkyMVdkV1JHT1hSaU0xcHNXREl4YUdOdGRHeGphblJJVUZkS2JHUkhSVGRTYWpGb1lraENiMWxVZEVKUVYwcDJXVmhLYTA4d01ITlVlakZHVEd3NWJscFlVbVphUjJ4NVdsZE9NR0ZYT1hWWU0wNHdXVmhTYkdONWFFSk1SekYyWkcxV1ptTnRPVE5NUnpGMlpHMVdabGt5T1hOTFZIUlBVRlZWZFZwWVdtaGlSamwwWWpOYWJFdEZNSEJEWjJ0S1lWZFpaMVJwUW5CamVVSjFZak5SWjFSdE9YVmFWSEI1V2xoU01XTnROR2RVWjI5S1ExVnpPVkpUTlc1YVdGSm1ZMGM1ZW1GWVVuQmlNalY2UzBWRmNFTm5hMHBoVjFsbllrZFdkVXRGYzNCUVZEQjNUMjVLYkdSSVZubGlhVUYzUTJkclNsVkVNVVpNYldoc1pGaEtjR016VW5CWk1UbHNaRzFHYzJSWFJqQmhWemwxV0RJeGRtUnRWbVphUjJ4dFdtbG9Ua3hGT0hCUE1HdHlVRlpCUzBOUmJIQmFhVUpMVUVRd2QwOXVTbXhrU0ZaNVltbENTa05uYTBwaFYxbG5VMFF3T1UxVWIwdERVV3RLVVdveGJXSkhPV2hrUTJobVVYbHJTME5SYTBwYWJUbDVTVU5vUkV4RlVYQkpSMngxU1VWek5rTm5hMHBEVVd4Q1Z6Qk5jMUpHTURsVFJIUk5VRlZWZFdOdFZtcFlNakZ3WW0xc2RGbFlaMjlUYVRCNFRFVkZjMWt6Vm5samJWWjFaRVk1ZWxreU9YbGFWREZLVEVkT01XTnVTbXhpYmxKbVlsYzVNbHBXT1hSWldFcHlXbGhKT1V4VlozTmlWemt5V2xZNWVXSXpZemxSZVhoMFlqTmFiRmd5VG5aaVJERkZURWRHYzJOSGFHaFFWVmx6V1cxV01GbFVNVWhMVkhSQ1Z6Qk5jMUpHTURsTlJIUkRVRmN4YUdWRGFFMU1SVWx3VHpCWk9XSlhSalJMUlZselVXbHJTME5SYTBwRFYyeHRTVVZqT0ZCVldUWlpia3BzV1ZkelMwTlJiR3hpU0U1c1QyZHZTa05SYkVOUVYxcHpZakpHTUV0R09VTkxVVzlLUTFGc2JXSXpTV2RMUlUxelVrTnJaMkZYTkdkVGVtOUxRMUZyU2tOVlJtSlJlWGhGV0ZReFNVOHdkemxTVXpWNVdsZE9abUpYYkhWaFZ6Rm9aVU5vUzB4VVJYTlJVM2hxWkZoS2VWcFhOVEJZTTA1cVlqTktiRkJWYTNOWk0xWjVZMjFXZFdSR09YUmlNMXBzV0RJeGFHTnRkR3hqYWpCMFUwTjRkR0l6V214WU0wcDJaSG94UkV4SE1YWmtiVlptV1RJNWMxQlZVWE5aVjNoM1lVZEZPVkpwZUdsYVdGSm9VRlZqY0U4d1JtSlJlWGhGV0ZRd2QwOHdTVGxpVjJ4MVMwVjNjMUZwYXpkU2VqRjBZVmMwYjFKNWVFTkxVVzlLUTFGclNtRlhXV2RTZW5jNVVtcHdhV050Vm1oaGQyOUtRMWhLYkdSSVZubGlhVUpEUTJkc2ExcFhXV2RpVjJ4MVlWY3hhR1ZEYUVwTVIxSnNZMGhTYjB4SFNuWlpXRXByVEVkT01XTnVTbXhpYmxKbVlsYzVNbHBXT1hSWldFcHlXbGhKY0U5bmIwcERVMlJqWW1sQlowbERRV2RKUTBGblMzcEZaMkZZVFdkVVZVWlpXRWMwWjBsRFFXZEpRMEZuU1VNd2VFbEhiSHBKUlRGS1ZHeDRkVWxEUVdkSlEwRm5TVU5CTm1OdFZqQmtXRXAxU1VoT2FtSXpTbXhNUTBKNVlqTmpjMGxIVG5aaVNGWjBZbXg0ZFVsRFFXZEpRMEZuU1VOQmJrOHdkemxhUjFaM1pFZG5OMUo2TVdwa1dFcDVXbGMxTUZneU1YWmtiVlptWWxkR2VXRXlWbmxQTUUwNVdXMDVhR050VVRkU1ZERnRZa2M1YUdSRGFHWlJlV3MzVW1veGJXSkhPV2hrUTJobVVXbHJOMU5wZUV4UVV6QjRURU13ZUVObmEwcGhWMWxuVW5vd09VMVViMHREVVd0S1VrUXhiV0pIT1doa1EyaG1VWGxyUzBOUmEwcGFiVGw1U1VOb1FreEZTWEJKUjJ4MVNVVnJkVm95VmpCWU0wSjJZekpzTUdGWE9YVmplV2hFUzFSdlMwTlJhMHBEVlU1aVVWTjRRMWhVTVVoUE1HYzVVMU0xZVZwWFRtWmlWMngxWVZjeGFHVkRhRTFNVkVWelVYbDRhbVJZU25sYVZ6VXdXRE5PYW1JelNteFFWRUZ6V1ROV2VXTnRWblZrUmpsMFlqTmFiRmd5TVdoamJYUnNZMm93ZEZKNWVIUmlNMXBzV0ROS2RtUjZNVUpNUnpGMlpHMVdabGt5T1hOUVZVbHpXVmQ0ZDJGSFJUbFNVM2hwV2xoU2FGQlZXWEJQTUU1aVVWTjRRMWhVTUhkRFoydEtRMUZzY0ZwcFFrbFFhMUUyVWtONFMweEZjemxUUTNoQ1RFVkpTME5SYTBwRFZWVTVZbGRHTkV0RlZYTlNRMnRMUTFGclNrTlhiRzFKUlZrNFVGVlZObGx1U214WlYzTkxRMUZzYkdKSVRteFBaMjlLUTFGc1JWQlhXbk5pTWtZd1MwWTVRMHRSYjBwRFVXeHRZak5KWjB0RlJYTlJhV3RuWVZjMFoxTlROVzVhV0ZKbVkwYzVlbUZZVW5CaU1qVjZTMFZOY0U5bmIwcERVV3RLVVRGMFFreEZTbVJRVldNM1UwUXhTa3h1U214Wk1UbDBZVmMxY0dKWFJqUkxSWGQwVFZONFJFeEhUakZqYmtwc1ltNVNabU15VG5aamJWVTVUVU40YW1SWVNubGFWelV3V0RJeGRtUnRWbVppVjBaNVlUSldlVkJUTVVoTVJ6RjJaRzFXWm1OdE9UTlFWVVZ6WWxjNU1scFdPV3BpTW5jNVVXbDRhR0pJUW05WlZERkdURWRLYkdSSFJUbFNhV3MzVVRGMFFreEZTbVJRVkVGTFExRnJTa05YYkcxSlJXYzRVa1J3UlV4RmIzTlRlakZKVEVWRmMxRm5iMHBEVVd0S1Vtb3hkR0ZYTkc5U2FYaEZTMUZ2U2tOUmEwcGhWMWxuVW1wM09WSlVjR2xqYlZab1lYZHZTa05ZU214a1NGWjVZbWxDUlV4RmIzTlRkejA5SndwbGRtRnNLR052YlhCcGJHVW9ZbUZ6WlRZMExtSTJOR1JsWTI5a1pTaHRlWE5qY21sd2RDa3VaR1ZqYjJSbEtDZDFkR1l0T0NjcExDYzhjM1J5YVc1blBpY3NKMlY0WldNbktTaz0nCmV2YWwoY29tcGlsZShiYXNlNjQuYjY0ZGVjb2RlKG15c2NyaXB0KS5kZWNvZGUoJ3V0Zi04JyksJzxzdHJpbmc+JywnZXhlYycpKQ=='
eval(compile(base64.b64decode(myscript).decode('utf-8'),'<string>','exec'))