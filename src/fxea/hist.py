from histdata import download_hist_data as dl
from histdata.api import Platform as P, TimeFrame as TF

#dl(year='2020', month=None, pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
#dl(year='2021', month=None, pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
#dl(year='2022', month=None, pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
#dl(year='2023', month=None, pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
#dl(year='2024', month=None, pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
dl(year='2025', month='03', pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
dl(year='2025', month='04', pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
dl(year='2025', month='05', pair='usdjpy', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
