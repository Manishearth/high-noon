# Route 66 locations

Overwatch recently published an animated short, [_Reunion_](https://www.youtube.com/watch?v=PKYVvPNhRR0), that takes place on the Route 66 map. In it, there's a standoff till [12PM](https://youtu.be/PKYVvPNhRR0?t=279), when everyone starts shooting.

12PM is significant for one of the main characters, Jesse McCree: McCree has an ability called "high noon" where in-game he says "it's high noon" and tries to shoot everyone in sight. Not too different from what's going on here. It's a reasonable assumption to make that the clock was shown as a symbolic nod towards this.

Except there's a mistake here, "high noon" &mdash; i.e. solar noon &mdash; is rarely exactly at 12PM, it can be quite off. However the short shows it happening at the stroke of noon to the second &mdash; this actually severely restricts the latitudes (and times) this event could have occurred on, if we assume this mistake to be canon.

["Historic Route 66" is a real thing](https://en.wikipedia.org/wiki/U.S._Route_66) -- it's now mostly I-40 and no longer called Route 66, but it used to exist and still has tourist spots along it talking about the time it was 66.

This repository contains code that calculates spots along Route 66 where such an event is possible. It assumes the Overwatch universe follows the same timezones and daylight savings time rules that ours does (but this can be configured).

## Results

The following table shows these latitudes, as well as the angle the sun makes against the celestial meridian in degrees at 12:00:00, 12:00:01, and 11:59:59. We consider high noon to be at 12:00:00 if it is closer to the celestial meridian than at the times one second off.

STATE |  TIME (UTC)         |  °W    | 12:00:00               |    12:00:01            |    11:59:59
------|---------------------|--------|------------------------|------------------------|------------------------
CA    | 2018-10-26 19:00:00 | 115.0  | -0.0019297558116022628 | -0.006109831583671621  | 0.0022300075719729044
CA    | 2018-06-23 19:00:00 | 114.92 | 0.0017798843902623446  | -0.0023942086751844727 | 0.005945776389041964
AZ    | 2018-03-23 19:00:00 | 111.76 | 0.00025089576644177214 | -0.0039155196272417925 | 0.0044173111601537585
AZ    | 2018-07-28 19:00:00 | 111.76 | 0.0014666694387130974  | -0.002699745954998889  | 0.005633084832425084
AZ    | 2018-01-13 19:00:00 | 111.75 | 0.00016893349641122768 | -0.003997481897300759  | 0.004335348890123214
NM    | 2018-05-20 18:00:00 | 108.4  | -0.001820472784913818  | -0.0059732278002684325 | 0.0023495519323921614
NM    | 2018-09-11 18:00:00 | 108.4  | -0.0007549632743462098 | -0.004907718289757668  | 0.003424648887404626
NM    | 2018-02-27 19:00:00 | 105.45 | 0.002067726085670074   | -0.0020986893080419122 | 0.00623414147938206
TX    | 2018-03-03 18:00:00 | 102.05 | -0.00012658587075975447| -0.004279340886114369  | 0.004050974191058654
TX    | 2018-02-08 18:00:00 | 102.04 | 0.00017377845011888395 | -0.004006133319307992  | 0.00434019376566135
TX    | 2018-10-26 17:00:00 | 101.91 | -0.001601906731480085  | -0.0057546617468346994 | 0.002571544961544977
TX    | 2018-05-31 17:00:00 | 101.85 | 0.0009600251095169436  | -0.003213831375603604  | 0.005126115335527419
TX    | 2018-04-15 17:00:00 | 101.84 | -0.0011374538678978752 | -0.00529020888325249   | 0.0030401664332971004
OK    | 2018-02-19 18:00:00 | 98.9   | -0.00040480239385942696| -0.004571217787571413  | 0.0037616129998525594
OK    | 2018-07-23 17:00:00 | 98.67  | 0.0014939901953994195  | -0.002672425198312567  | 0.005660405589111406
OK    | 2018-07-28 17:00:00 | 98.67  | 0.000264556144799144   | -0.0039018592489128423 | 0.00443097153851113
OK    | 2018-11-06 18:00:00 | 95.89  | 0.00023686210376510733 | -0.003924171049277447  | 0.004403239196470078



Route 66 extends past Oklahoma, but we know this occurs in the American Southwest, so we don't bother to calculate these latitudes past Oklahoma.

## Locations

These latitudes, intersected with where Route 66 used to be (i.e., I-40) give us the following locations for the Route 66 map in Overwatch:


 - [Slightly west of Needles, AZ, in California, near 114.9W 34.85N or 115W 34.85N](https://www.google.com/maps/place/34%C2%B051'00.0%22N+114%C2%B055'12.0%22W/@34.7914143,-114.8497319,46039m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d34.85!4d-114.92)
 - [Slightly west of Flagstaff, AZ, near 111.75W 35.2N](https://www.google.com/maps/place/35%C2%B012'00.0%22N+111%C2%B045'36.0%22W/@35.2388986,-111.8218234,23963m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d35.2!4d-111.76)
 - [West of Gallup, NM, near 108.4W 35.46N](https://www.google.com/maps/place/35%C2%B027'36.0%22N+108%C2%B024'00.0%22W/@35.3472887,-108.4623781,9.88z/data=!4m5!3m4!1s0x0:0x0!8m2!3d35.46!4d-108.4)
 - [East of Albuquerque, NM, near 105.45W 35N](https://www.google.com/maps/place/35%C2%B000'00.0%22N+105%C2%B027'00.0%22W/@34.8944304,-105.557479,102846m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d35!4d-105.45)
 - [In Amarillo, TX, near 101.85W 35.18N or 102.05W 35.18N](https://www.google.com/maps/place/35%C2%B010'48.0%22N+102%C2%B003'00.0%22W/@35.2094435,-101.7024998,153685m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d35.18!4d-102.05)
 - [East of Oklahoma City, OK, near 96.67 35.38N or 96.9W 35.38N](https://www.google.com/maps/place/35%C2%B022'48.0%22N+96%C2%B054'00.0%22W/@35.3365585,-96.9554006,9.54z/data=!4m5!3m4!1s0x0:0x0!8m2!3d35.38!4d-96.9)
 - [Further west of Oklahoma City, OK, south of Tulsa, near 95.89W 35.42N](https://www.google.com/maps/place/35%C2%B025'12.0%22N+95%C2%B053'24.0%22W/@34.6207603,-94.9211184,8.04z/data=!4m5!3m4!1s0x0:0x0!8m2!3d35.42!4d-95.89)

## Conclusion

The most likely one of these is [this one near Albuquerque](https://www.google.com/maps/place/35%C2%B000'00.0%22N+105%C2%B027'00.0%22W/@34.8944304,-105.557479,102846m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d35!4d-105.45), with[the one in the Mojave Desert](https://www.google.com/maps/place/34%C2%B051'00.0%22N+114%C2%B055'12.0%22W/@34.7914143,-114.8497319,46039m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d34.85!4d-114.92) or  [this one near Flagstaff](https://www.google.com/maps/place/35%C2%B012'00.0%22N+111%C2%B045'36.0%22W/@35.2388986,-111.8218234,23963m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d35.2!4d-111.76) coming close. The Mojave Desert and Red Rock State Park in Arizona have lots of red rock formations like the ones in the Route 66 map, some of them reasonably close to these coordinates. Albuquerque also has similar stuff, with the formations being much closer to the actual highway.


