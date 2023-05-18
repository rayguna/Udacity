### Explore Close Approaches of Near-Earth Objects

This CLI program searches for and explores close approaches of near-Earth objects (NEOs) using two sets of data. 

#### The Dataset

One dataset (`neos.csv`) contains information about semantic, physical, orbital, and model parameters for certain small bodies (asteroids and comets, mostly) in our solar system. The other dataset (`cad.json`) contains information about NEO close approaches when the orbit of an astronomical body brings it close to Earth. Please refer to the [glossary](https://cneos.jpl.nasa.gov/glossary/) to define any unfamiliar terms.

The program can inspect the properties of the near-Earth objects in the data set and query the data set of close approaches to Earth using any combination of the following filters:

- Occurs on a given date.
- Occurs on or after a given start date.
- Occurs on or before a given end date.
- Approaches Earth at a distance of at least (or at most) X astronomical units.
- Approaches Earth at a relative velocity of at least (or at most) Y kilometers per second.
- Has a diameter that is at least as large as (or at least as small as) Z kilometers.
- Is marked by NASA as potentially hazardous (or not).

The first three rows of `neos.csv` is as follows. The first NEO has a primary designation of 433 and an IAU name "Eros". It is ('Y') an NEO, not ('N') potentially hazardous, and has a diameter of 16.84km. In some cases, the fields are missing as this information is not available.

```
id,spkid,full_name,pdes,name,prefix,neo,pha,H,G,M1,M2,K1,K2,PC,diameter,extent,albedo,rot_per,GM,BV,UB,IR,spec_B,spec_T,H_sigma,diameter_sigma,orbit_id,epoch,epoch_mjd,epoch_cal,equinox,e,a,q,i,om,w,ma,ad,n,tp,tp_cal,per,per_y,moid,moid_ld,moid_jup,t_jup,sigma_e,sigma_a,sigma_q,sigma_i,sigma_om,sigma_w,sigma_ma,sigma_ad,sigma_n,sigma_tp,sigma_per,class,producer,data_arc,first_obs,last_obs,n_obs_used,n_del_obs_used,n_dop_obs_used,condition_code,rms,two_body,A1,A2,A3,DT
a0000433,2000433,"   433 Eros (A898 PA)",433,Eros,,Y,N,10.4,0.46,,,,,,16.84,34.4x11.2x11.2,0.25,5.270,4.463e-04,0.921,0.531,,S,S,,0.06,"JPL 658",2459000.5,59000,20200531.0000000,J2000,.2229512647434284,1.458045729081037,1.132972589728666,10.83054121829922,304.2993259000444,178.8822959227224,271.0717325705167,1.783118868433408,.5598186418120109,2459159.351922368362,20201105.8519224,643.0654021001488,1.76061711731731,.148623,57.83961291,3.2865,4.582,9.6497E-9,2.1374E-10,1.4063E-8,1.1645E-6,3.8525E-6,4.088E-6,1.4389E-6,2.6139E-10,1.231E-10,2.5792E-6,1.414E-7,AMO,Giorgini,46330,1893-10-29,2020-09-03,8767,4,2,0,.28397,,,,,
a0000719,2000719,"   719 Albert (A911 TB)",719,Albert,,Y,N,15.5,,,,,,,,,,5.801,,,,,S,,,,"JPL 214",2459000.5,59000,20200531.0000000,J2000,.5465584653041263,2.63860206439375,1.196451769530403,11.56748478123323,183.8669499802364,156.17633771,140.2734217745985,4.080752359257098,.2299551959241748,2458390.496728663387,20180928.9967287,1565.522355575327,4.28616661348481,.203482,79.18908994,1.41794,3.140,2.1784E-8,2.5313E-9,5.8116E-8,2.9108E-6,1.6575E-5,1.6827E-5,2.5213E-6,3.9148E-9,3.309E-10,1.0306E-5,2.2528E-6,AMO,"Otto Matic",39593,1911-10-04,2020-02-27,1874,,,0,.39148,,,,,
```

The definition of just a few of the above columns are as follows:

```
pdes - the primary designation of the NEO. This is a unique identifier in the database, and its "name" to computer systems.
name - the International Astronomical Union (IAU) name of the NEO. This is its "name" to humans.
pha - whether NASA has marked the NEO as a "Potentially Hazardous Asteroid," roughly meaning that it's large and can come quite close to Earth.
diameter - the NEO's diameter (from an equivalent sphere) in kilometers.
```

Below shows a peek of the `cad.json` dataset. The first entry of the dataset below has the following interpretations:

- an asteroid or comet with primary designation "170903"
- an orbit ID of 105
- a close approach time of 2415020.507669610 (in JD Ephemeris time) or 1900-Jan-01 00:11 (in a normal format)
- an approach distance of 0.0921795123769547 astronomical units (with 3-sigma bounds of (0.0912006569517418au, 0.0931589328621254au))
- an approach velocity of 16.7523040362574 km/s (relative to Earth) or 16.7505784933163 km/s (relative to a massless body)
- 3-sigma uncertainty in the time of close approach of 1 hour
- an absolute magnitude of 18.1

```json
{
  "signature":{
    "source":"NASA/JPL SBDB Close Approach Data API",
    "version":"1.1"
  },
  "count":"406785",
  "fields":["des", "orbit_id", "jd", "cd", "dist", "dist_min", "dist_max", "v_rel", "v_inf", "t_sigma_f", "h"],
  "data":[
    [
       "170903",
       "105",
       "2415020.507669610",
       "1900-Jan-01 00:11",
       "0.0921795123769547",
       "0.0912006569517418",
       "0.0931589328621254",
       "16.7523040362574",
       "16.7505784933163",
       "01:00",
       "18.1"
    ],
    [
       "2005 OE3",
       "52",
       "2415020.606013490",
       "1900-Jan-01 02:33",
       "0.414975519685102",
       "0.414968315685577",
       "0.414982724454678",
       "17.918395877175",
       "17.9180375373357",
       "< 00:01",
       "20.3"
    ],
    ...
  ]
}
```

The definition of each of the fields is as follows (https://ssd-api.jpl.nasa.gov/doc/cad.html):

- des - primary designation of the asteroid or comet (e.g., 443, 2000 SG344)
- orbit_id - orbit ID
- jd - time of close-approach (JD Ephemeris Time)
- cd - time of close-approach (formatted calendar date/time, in UTC)
- dist - nominal approach distance (au)
- dist_min - minimum (3-sigma) approach distance (au)
- dist_max - maximum (3-sigma) approach distance (au)
- v_rel - velocity relative to the approach body at close approach (km/s)
- v_inf - velocity relative to a massless body (km/s)
- t_sigma_f - 3-sigma uncertainty in the time of close-approach (formatted in days, hours, and minutes; days are not included if zero; example "13:02" is 13 hours 2 minutes; example "2_09:08" is 2 days 9 hours 8 minutes)
- h - absolute magnitude H (mag)

#### The Files Structure

The files structure is as follows:

```
.
├── README.md       # This file.
├── main.py
├── models.py       
├── read.py         
├── database.py     
├── filters.py      
├── write.py        
├── helpers.py
├── data
│   ├── neos.csv
│   └── cad.json
└── tests
    ├── test-neos-2020.csv
    ├── test-cad-2020.json
    ├── test_*.py
    ├── ...
    └── test_*.py
```

### Testing the Program

The program has been tested using the command, python -m unittest --verbose tests.test_extract tests.test_database

```
test_approach_distance_is_float (tests.test_extract.TestLoadApproaches) ... ok
test_approach_time_is_datetime (tests.test_extract.TestLoadApproaches) ... ok
test_approach_velocity_is_float (tests.test_extract.TestLoadApproaches) ... ok
test_approaches_are_collection (tests.test_extract.TestLoadApproaches) ... ok
test_approaches_contain_all_elements (tests.test_extract.TestLoadApproaches) ... ok
test_approaches_contain_close_approaches (tests.test_extract.TestLoadApproaches) ... ok
test_adonis_is_potentially_hazardous (tests.test_extract.TestLoadNEOs) ... ok
test_asclepius_has_name_no_diameter (tests.test_extract.TestLoadNEOs) ... ok
test_neos_are_collection (tests.test_extract.TestLoadNEOs) ... ok
test_neos_contain_2019_SC8_no_name_no_diameter (tests.test_extract.TestLoadNEOs) ... ok
test_neos_contain_all_elements (tests.test_extract.TestLoadNEOs) ... ok
test_neos_contain_near_earth_objects (tests.test_extract.TestLoadNEOs) ... ok
test_database_construction_ensures_each_neo_has_an_approaches_attribute (tests.test_database.TestDatabase) ... ok
test_database_construction_ensures_neos_collectively_exhaust_approaches (tests.test_database.TestDatabase) ... ok
test_database_construction_ensures_neos_mutually_exclude_approaches (tests.test_database.TestDatabase) ... ok
test_database_construction_links_approaches_to_neos (tests.test_database.TestDatabase) ... ok
test_get_neo_by_designation (tests.test_database.TestDatabase) ... ok
test_get_neo_by_designation_missing (tests.test_database.TestDatabase) ... ok
test_get_neo_by_designation_neos_with_year (tests.test_database.TestDatabase) ... ok
test_get_neo_by_name (tests.test_database.TestDatabase) ... ok
test_get_neo_by_name_missing (tests.test_database.TestDatabase) ... ok

----------------------------------------------------------------------
Ran 21 tests in 3.864s

OK
```

#### Running the Program

Run the program at the command line as `python3 main.py ... ... ...` to yield the following output:

To get an explanation on how to invoke the scipt, type `python3 main.py --help`

```
usage: main.py [-h] [--neofile NEOFILE] [--cadfile CADFILE] {inspect,query,interactive} ...

Explore past and future close approaches of near-Earth objects.

positional arguments:
  {inspect,query,interactive}

optional arguments:
  -h, --help            show this help message and exit
  --neofile NEOFILE     Path to CSV file of near-Earth objects.
  --cadfile CADFILE     Path to JSON file of close approach data.
```
