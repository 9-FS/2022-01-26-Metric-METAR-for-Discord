import KFS
import re
from weather_minimums import WEATHER_MIN


def change_format_VV(info: str) -> str|None:
    re_match: re.Match|None


    #VV [100ft]
    re_match=re.search("^VV(?P<VV>[0-9]{3})$", info)
    if re_match!=None:
        info_new: str
        VV: float=int(re_match.groupdict()["VV"])*100*KFS.convert_to_SI.length["ft"]


        info_new=f"VV{KFS.fstr.notation_abs(VV, 2)}m"

        if "vis" in WEATHER_MIN and VV<WEATHER_MIN["vis"]:  #if visibility below minimums: mark
            info_new=f"**{info_new}**"
        return f" {info_new}"


    #russia: QBB, VV [m]
    re_match=re.search("^QBB(?P<QBB>[0-9]{3})$", info)
    if re_match!=None:
        info_new: str
        QBB: int=int(re_match.groupdict()["QBB"])
        
        
        info_new=f"QBB{KFS.fstr.notation_abs(QBB, 2)}m"
        
        if "vis" in WEATHER_MIN and QBB<WEATHER_MIN["vis"]: #if visibility below minimums: mark
            info_new=f"**{info_new}**"
        return f" {info_new}"