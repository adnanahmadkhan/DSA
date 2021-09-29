select * from EKATA_V2_AR limit 100;

select * from EKATA_V2_AR where is_commercial = 0 limit 1;

show create table EKATA_V2_AR;

select * from SN_EKATA_V2_AR_TEST limit 100;

select distinct(EffectiveDateTime) from PORT_DATA_GRF_US where EffectiveDateTime>= '2021-05-27';

select count(*) from EKATA_V2_DELIVERY;

select * from Throtle limit 10;
