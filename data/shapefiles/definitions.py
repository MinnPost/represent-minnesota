from datetime import date
import boundaries
import processing

# state house
boundaries.register('State House districts (2012)',  # The string to be used for
    # the boundary set's slug. The slug will be "federal-electoral-districts".

    # (Optional) The path to the shapefile's directory relative to this file.
    # If this definition file and the shapefile share the same directory, you
    # can omit this parameter, or set it to the empty string.
    file='state-house-districts/2012-mn_leg_gis/L2012/',
    # (Optional) The encoding of the shapefile's attributes. The default is
    # "ascii", but many shapefiles are encoded as "iso-8859-1".
    #encoding='iso-8859-1',
    # (Optional) Override the Spatial Reference System Identifier (SRID) of
    # the shapefile.
    #srid='',


    # The following Boundary Set fields will be made available via the API.

    # The most recent date on which the data was updated.
    last_updated=date(2012, 5, 3),
    # The plural name of the boundary set, for display. By default, it will use
    # the boundary set's slug.
    name='State House districts (2012)',
    # A generic singular name for a boundary in the set. If the boundary set's
    # name ends in "s", this parameter is optional, as is the case here.
    singular='State House district (2012)',

    # (Optional) The geographic area covered by the boundary set, which is
    # often a country, a region, a municipality, etc.
    domain='Minnesota',
    # (Optional) The entity responsible for publishing the data.
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    # (Optional) A URL to the source of the data.
    source_url='http://www.gis.leg.mn/redist2010/plans.html',
    # (Optional) A URL to the licence under which the data is made available.
    #licence_url='http://data.gc.ca/eng/open-government-licence-canada',
    # (Optional) The date from which the set's boundaries are in effect.
    #start_date=None,
    # (Optional) The date until which the set's boundaries are in effect.
    #end_date=None,
    # (Optional) Free-form text notes, often used to describe changes that were
    # made to the original source data, e.g. deleted or merged features.
    notes='These districts were defined in 2012.',
    # (Optional) Any additional metadata to include in API responses.
    #extra={'id': 'ocd-division/country:ca'},


    # The following Boundary functions take a feature as an argument and return
    # an appropriate value as described below.
    #
    # In this case, we use helper functions to access and clean attributes from
    # the shapefile:
    #
    # * `attr` retrieves a feature's attribute without making changes.
    # * `clean_attr` title-cases a string if it is all-caps, normalizes
    #   whitespace, and normalizes long dashes.
    # * `dashed_attr` does the same as `clean_attr`, but replaces all hyphens
    #   with long dashes.
    #
    # If you want to write your own function, set for example `name_func=namer`
    # and define a function that looks like:
    #
    # def namer(f):
    #   return f.get('FEDENAME')

    # A function that returns a feature's name.
    name_func=boundaries.clean_attr('district'),

    # (Optional) A function that returns a feature's identifier, which should
    # be unique across the features in the shapefile and relatively stable
    # across time: for example, a district number or a geographic code. By
    # default, features have no identifiers.
    id_func=boundaries.attr('id'),
    # (Optional) A function that returns a feature's slug (the last part of its
    # URL path). By default, it will use the feature's name.
    slug_func=boundaries.attr('district'),
    # (Optional) A function that returns whether a feature should be loaded. By
    # default, all features are loaded.
    #is_valid_func=lambda feature: True,
    # (Optional) A function that returns the Point at which to place a label
    # for the boundary, in EPSG:4326.
    #label_point_func=lambda feature: None,
)
boundaries.register('State House districts (2022)',
    file='state-house-districts/2022-state-house-districts',
    last_updated=date(2022, 2, 15),
    name='State House districts (2022)',
    singular='State House district (2022)',
    domain='Minnesota',
    authority='Minnesota Judicial Branch Special Redistricting Panel 2021',
    source_url='https://www.mncourts.gov/2021RedistrictingPanel',
    notes='This shapefile was built from the block equivalency files released by the redistricting panel, using census block data from the Legislative Coordinating Commission.',
    name_func=boundaries.attr('DistrictID'),
    id_func=boundaries.attr('DistrictID'),
    slug_func=boundaries.attr('DistrictID')
)

# State Senate
boundaries.register('State Senate districts (2012)', 
    file='state-senate-districts/2012-mn_leg_gis/S2012/',
    last_updated=date(2012, 5, 3),
    name='State Senate districts (2012)',
    singular='State Senate district (2012)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    source_url='http://www.gis.leg.mn/redist2010/plans.html',
    notes='These districts were defined in 2012.',
    name_func=boundaries.clean_attr('district'),
    id_func=boundaries.attr('district'),
    slug_func=boundaries.attr('district'),
)
boundaries.register('State Senate districts (2022)',
    file='state-senate-districts/state-senate-2022',
    last_updated=date(2022, 2, 15),
    name='State Senate districts (2022)',
    singular='State Senate district (2022)',
    domain='Minnesota',
    authority='Minnesota Judicial Branch Special Redistricting Panel 2021',
    source_url='https://www.mncourts.gov/2021RedistrictingPanel',
    notes='This shapefile was built from the block equivalency files released by the redistricting panel, using census block data from the Legislative Coordinating Commission.',
    name_func=boundaries.attr('DistrictID'),
    id_func=boundaries.attr('DistrictID'),
    slug_func=boundaries.attr('DistrictID')
)

# Congress
boundaries.register('Congressional districts (2002)', 
    file='congressional-districts/2002-census/tl_2010_27_cd111/',
    last_updated=date(2012, 5, 3),
    name='Congressional districts (2002)',
    singular='Congressional district (2002)',
    domain='Minnesota',
    authority='U.S. Census Bureau TIGER lines',
    source_url='http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
    notes='These districts were defined in 2002.',
    name_func=boundaries.clean_attr('cd111fp'),
    id_func=boundaries.attr('geoid10'),
    slug_func=boundaries.attr('cd111fp'),
)
boundaries.register('Congressional districts (2012)',
    file='congressional-districts/2012-mn_leg_gis/C2012/',
    last_updated=date(2012, 5, 3),
    name='Congressional districts (2012)',
    singular='Congressional district (2012)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    source_url='http://www.gis.leg.mn/redist2010/plans.html',
    notes='These districts were defined in 2012.',
    name_func=boundaries.clean_attr('district'),
    id_func=boundaries.attr('id'),
    slug_func=boundaries.attr('district'),
)
boundaries.register('Congressional districts (2022)',
    file='congressional-districts/c2022-shp/',
    last_updated=date(2022, 2, 15),
    name='Congressional districts (2022)',
    singular='Congressional district (2022)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    source_url='http://www.gis.leg.mn/redist2020/plans.html',
    notes='These districts were defined in 2022.',
    name_func=boundaries.clean_attr('district'),
    id_func=boundaries.attr('id'),
    slug_func=boundaries.attr('district'),
)

# School districts
boundaries.register('School districts (2010)',
    file='school-districts/2010-census/',
    last_updated=date(2012, 5, 3),
    name='School districts (2010)',
    singular='School district (2010)',
    domain='Minnesota',
    authority='U.S. Census Bureau TIGER lines',
    source_url='http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
    notes='These districts were defined in 2012.',
    name_func=boundaries.clean_attr('geoid10'),
    id_func=boundaries.attr('geoid10'),
    slug_func=boundaries.attr('geoid10'),
)
boundaries.register('School districts (2012)',
    file='school-districts/2012-mngeo/',
    last_updated=date(2012, 7, 18),
    name='School districts (2012)',
    singular='School district (2012)',
    domain='Minnesota',
    authority='MN Geo and Minnesota Department of Education',
    source_url='http://www.mngeo.state.mn.us/chouse/metadata/sd12.html',
    notes='Aitkin and Minneapolis share the same ID, so Minneapolis is 1-1.',
    name_func=processing.simple_index_namer(['sdnum']),
    id_func=processing.simple_index_namer(['sdnum']),
    slug_func=processing.simple_index_namer(['sdnum']),
)
boundaries.register('School districts (2013)',
    file='school-districts/2013-mn-leg/',
    last_updated=date(2013, 10, 10),
    name='School districts (2013)',
    singular='School district (2013)',
    domain='Minnesota',
    authority='MN State Legislature and Minnesota Department of Education',
    source_url='http://www.gis.leg.mn/html/download.html',
    notes='Aitkin and Minneapolis share the same ID, so Minneapolis is 1-1.',
    name_func=processing.simple_index_namer(['sdnum']),
    id_func=processing.simple_index_namer(['sdnum']),
    slug_func=processing.simple_index_namer(['sdnum']),
)
boundaries.register('School districts (2018)',
    file='school-districts/2018-mngeo',
    last_updated=date(2018, 10, 22),
    name='School districts (2018)',
    singular='School district (2018)',
    domain='Minnesota',
    authority='Minnesota Department of Education',
    source_url='https://gisdata.mn.gov/dataset/bdry-school-district-boundaries',
    notes='Aitkin and Minneapolis share same ID',
    name_func=processing.simple_index_namer(['UNI_MAJ']),
    id_func=processing.simple_index_namer(['UNI_MAJ']),
    slug_func=processing.simple_index_namer(['UNI_MAJ']),
)
boundaries.register('School districts (2021)',
    file='school-districts/2021-mngeo',
    last_updated=date(2021, 11, 9),
    name='School districts (2021)',
    singular='School district (2021)',
    domain='Minnesota',
    authority='Minnesota Department of Education',
    source_url='https://gisdata.mn.gov/dataset/bdry-school-district-boundaries',
    notes='Aitkin and Minneapolis share same ID',
    name_func=processing.simple_index_namer(['SDNUMBER']),
    id_func=processing.simple_index_namer(['SDNUMBER']),
    slug_func=processing.simple_index_namer(['SDNUMBER']),
)

# Counties
boundaries.register('Counties (2010)',
    file='counties/2010-mn-gis-leg/',
    last_updated=date(2012, 11, 12),
    name='Counties (2010)',
    singular='County (2010)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    source_url='http://www.gis.leg.mn/metadata/county2010.htm',
    notes='The County ID used is the Minnesota count code, as opposed to the Census code.',
    name_func=processing.simple_index_namer(['data']),
    id_func=processing.simple_index_namer(['data']),
    slug_func=processing.simple_index_namer(['data']),
)

# State parks
boundaries.register('State parks (2002)',
    file='state-parks/2002-mn-dnr/',
    last_updated=date(2012, 6, 22),
    name='State parks (2002)',
    singular='State park (2002)',
    domain='Minnesota',
    authority='Minnesota Department of Natural Resources (DNR)',
    source_url='http://deli.dnr.state.mn.us/metadata.html?id=L220000190201',
    notes='',
    name_func=boundaries.clean_attr('pgm_prj'),
    id_func=boundaries.attr('pgm_prj'),
    slug_func=boundaries.attr('pgm_prj'),
)

# National forests
boundaries.register('National forests (2008)',
    file='national-forests/2008-mn-dnr/',
    last_updated=date(2012, 6, 22),
    name='National forests (2008)',
    singular='National forest (2008)',
    domain='Minnesota',
    authority='Minnesota Department of Natural Resources (DNR)',
    source_url='http://deli.dnr.state.mn.us/metadata.html?id=L220000110201',
    notes='',
    name_func=processing.simple_index_namer(['region', 'forest_num'], normalizer=lambda x: x.lstrip('0')),
    id_func=processing.simple_index_namer(['region', 'forest_num'], normalizer=lambda x: x.lstrip('0')),
    slug_func=processing.simple_index_namer(['region', 'forest_num'], normalizer=lambda x: x.lstrip('0')),
)

# Voting precincts (will take awhile)
boundaries.register('Voting precincts (2010)',
    file='voting-precincts/2010-mn_leg_gis/',
    last_updated=date(2012, 6, 22),
    name='Voting precincts (2010)',
    singular='Voting precinct (2010)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office and Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2010.htm',
    notes='',
    name_func=boundaries.clean_attr('district'),
    id_func=boundaries.attr('district'),
    slug_func=boundaries.attr('district'),
)
boundaries.register('Voting precincts (2012)',
    file='voting-precincts/2012-mn_sos/',
    last_updated=date(2012, 7, 24),
    name='Voting precincts (2012)',
    singular='Voting precinct (2012)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2012.htm',
    notes='A couple precincts in Makota did not have a proper ID so it was manually added assuming a specific identification scheme.',
    name_func=boundaries.clean_attr('vtd'),
    id_func=boundaries.attr('vtd'),
    slug_func=boundaries.attr('vtd'),
)
boundaries.register('Voting precincts (2014)',
    file='voting-precincts/2014-mn_sos/',
    last_updated=date(2014, 9, 24),
    name='Voting precincts (2014)',
    singular='Voting precinct (2014)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2014.htm',
    notes='',
    name_func=boundaries.clean_attr('vtdid'),
    id_func=boundaries.attr('vtdid'),
    slug_func=boundaries.attr('vtdid'),
)
boundaries.register('Voting precincts (2016)',
    file='voting-precincts/2016-mn_sos/',
    last_updated=date(2016, 10, 25),
    name='Voting precincts (2016)',
    singular='Voting precinct (2016)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2016.htm',
    notes='',
    name_func=boundaries.clean_attr('vtdid'),
    id_func=boundaries.attr('vtdid'),
    slug_func=boundaries.attr('vtdid'),
)
boundaries.register('Voting precincts (2018)',
    file='voting-precincts/2018-mn_sos/',
    last_updated=date(2018, 2, 1),
    name='Voting precincts (2018)',
    singular='Voting precinct (2018)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2018.htm',
    notes='',
    name_func=boundaries.clean_attr('vtdid'),
    id_func=boundaries.attr('vtdid'),
    slug_func=boundaries.attr('vtdid'),
)
boundaries.register('Voting precincts (2020)',
    file='voting-precincts/2020-redistricting/',
    last_updated=date(2021, 10, 8),
    name='Voting precincts (2020)',
    singular='Voting precinct (2020)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='https://gisdata.mn.gov/dataset/society-redistricting-2020',
    notes='redistricting zip includes mcd files',
    name_func=boundaries.clean_attr('VTD'),
    id_func=boundaries.attr('VTD'),
    slug_func=boundaries.attr('VTD'),
)
boundaries.register('Voting precincts (2022)',
    file='voting-precincts/2022-mn_sos/',
    last_updated=date(2022, 9, 1),
    name='Voting precincts (2022)',
    singular='Voting precinct (2022)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='https://gisdata.mn.gov/dataset/bdry-votingdistricts',
    notes='',
    name_func=boundaries.clean_attr('vtdid'),
    id_func=boundaries.attr('vtdid'),
    slug_func=boundaries.attr('vtdid'),
)

# Minor civic divisons (cities and towns) (will take awhile)
boundaries.register('Minor civil divisions (2010)',
    file='minor-civil-divisions/2010-mn_leg_gis/',
    last_updated=date(2012, 6, 22),
    name='Minor civil divisions (2010)',
    singular='Minor civil division (2010)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    source_url='http://www.gis.leg.mn/metadata/mcd2010.htm',
    notes='Minor civil divisions are also considered cities and townships.',
    name_func=boundaries.clean_attr('mcd'),
    id_func=boundaries.attr('mcd'),
    slug_func=boundaries.attr('mcd'),    
)

# District courts
boundaries.register('District courts (2008)',
    file='district-courts/2008-mn_gis_leg/',
    last_updated=date(2012, 7, 13),
    name='District courts (2008)',
    singular='District court (2008)',
    domain='Minnesota',
    authority='Minnesota Legislative Coordinating Commission - GIS Office',
    source_url='http://gis.leg.mn/',
    notes='Emailed directly from the MN Leg GIS dept.  Edited to add more descriptive name.',
    name_func=processing.simple_index_namer(['judicial']),
    id_func=processing.simple_index_namer(['judicial']),
    slug_func=processing.simple_index_namer(['judicial']),
)
boundaries.register('District courts (2012)',
    file='district-courts/2012-mn_sos/',
    last_updated=date(2012, 7, 24),
    name='District courts (2012)',
    singular='District court (2012)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2012.htm',
    notes='This dataset was derived from the 2012 voting precincts dataset.',
    name_func=processing.simple_index_namer(['juddist'], normalizer=lambda x: x.lstrip('0')),
    id_func=processing.simple_index_namer(['juddist'], normalizer=lambda x: x.lstrip('0')),
    slug_func=processing.simple_index_namer(['juddist'], normalizer=lambda x: x.lstrip('0')),
)

# Zip codes
boundaries.register('ZIP codes (2010)',
    file='zipcodes/2010-census/',
    last_updated=date(2012, 7, 18),
    name='ZIP codes (2010)',
    singular='Zip code (2010)',
    domain='Minnesota',
    authority='U.S. Census Bureau TIGER lines',
    source_url='ftp://ftp2.census.gov/geo/tiger/TIGER2010/ZCTA5/2010/',
    notes='',
    name_func=boundaries.clean_attr('ZCTA5CE10'),
    id_func=boundaries.attr('ZCTA5CE10'),
    slug_func=boundaries.attr('ZCTA5CE10'), 
)

# County Commissioner districts
boundaries.register('County Commissioner districts (2012)',
    file='county-commissioner/2012-mn_sos/',
    last_updated=date(2012, 7, 24),
    name='County Commissioner districts (2012)',
    singular='County Commissioner district (2012)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2012.htm',
    notes='This dataset was derived from the 2012 voting precincts dataset.',
    name_func=processing.simple_index_namer(['ccd_id'], normalizer=lambda x: x.lstrip('0')),
    id_func=processing.simple_index_namer(['ccd_id'], normalizer=lambda x: x.lstrip('0')),
    slug_func=processing.simple_index_namer(['ccd_id'], normalizer=lambda x: x.lstrip('0')),    
)

# Hospital districts
boundaries.register('Hospital districts (2012)',
    file='hospitals/2012-mn_sos/',
    last_updated=date(2012, 7, 24),
    name='Hospital districts (2012)',
    singular='Hospital district (2012)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2012.htm',
    notes='This dataset was derived from the 2012 voting precincts dataset.',
    name_func=processing.simple_index_namer(['hospdist'], normalizer=lambda x: x.lstrip('0')),
    id_func=processing.simple_index_namer(['hospdist'], normalizer=lambda x: x.lstrip('0')),
    slug_func=processing.simple_index_namer(['hospdist'], normalizer=lambda x: x.lstrip('0')),  
)

# Soil and water districts
boundaries.register('Soil and Water districts (2012)',
    file='soil-water/2012-mn_sos/',
    last_updated=date(2012, 7, 24),
    name='Soil and Water districts (2012)',
    singular='Soil and Water district (2012)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2012.htm',
    notes='This dataset was derived from the 2012 voting precincts dataset.',    
    name_func=processing.simple_index_namer(['soilwdist'], normalizer=lambda x: x.lstrip('0')),
    id_func=processing.simple_index_namer(['soilwdist'], normalizer=lambda x: x.lstrip('0')),
    slug_func=processing.simple_index_namer(['soilwdist'], normalizer=lambda x: x.lstrip('0')), 
)

# Wards
# In theory the id for this should be the MCD code with the Ward code, but
# since the MCD code is not with the data, then we use the MCD name
boundaries.register('Wards (2012)',
    file='wards/2012-mn_sos/',
    last_updated=date(2012, 7, 24),
    name='Wards (2012)',
    singular='Ward (2012)',
    domain='Minnesota',
    authority='Minnesota Secretary of State',
    source_url='http://www.gis.leg.mn/metadata/vtd2012.htm',
    notes='This dataset was derived from the 2012 voting precincts dataset.',    
    name_func=processing.simple_index_namer(['ward_id'], normalizer=lambda x: x.lstrip('0')),
    id_func=processing.simple_index_namer(['ward_id'], normalizer=lambda x: x.lstrip('0')),
    slug_func=processing.simple_index_namer(['ward_id'], normalizer=lambda x: x.lstrip('0')), 
)

# Minneapolis council wards 2022
# Ideally will be replaced when the statewide wards data set above is updated for 2022.
# Adding this now for redistricting analysis purposes.
boundaries.register('Minneapolis Council Wards (2022)',
    file='wards/minneapolis-council-wards-2022/',
    last_updated=date(2022, 3, 3),
    name='Minneapolis Council Wards (2022)',
    singular='Minneapolis Council Ward (2022)',
    domain='Minnesota',
    authority='Minneapolis Charter Commission',
    source_url='https://www.minneapolismn.gov/government/programs-initiatives/redistricting/',
    notes='This dataset comes from the redisctr map created by the city Redistricting Group',
    name_func=boundaries.attr('districtr'),
    id_func=boundaries.attr('districtr'),
    slug_func=boundaries.attr('districtr')
)

# Minneapolis neighborhoods
boundaries.register('Minneapolis Neighborhoods (2013)',
    file='neighborhoods/2013-minneapolis-neighborhoods/',
    last_updated=date(2013, 6, 4),
    name='Minneapolis Neighborhoods (2013)',
    singular='Minneapolis Neighborhood (2013)',
    domain='Minnesota',
    authority='City of Minneapolis',
    source_url='http://www.minneapolismn.gov/maps/about_maps_public-maps-links',
    notes='This dataset was was altered to create unique descriptive IDs for each neighborhood for better referencing.',
    name_func=boundaries.clean_attr('neighbor_1'),
    id_func=boundaries.attr('neighbor_1'),
    slug_func=boundaries.attr('neighbor_1'), 
)

# St. Paul district councils (neighborhoods)
boundaries.register('St. Paul District Councils (2012)',
    file='neighborhoods/2012-st-paul-district-councils/',
    last_updated=date(2013, 6, 4),
    name='St. Paul District Councils (2012)',
    singular='St. Paul District Council (2012)',
    domain='Minnesota',
    authority='City of St. Paul',
    source_url='http://stpaul.gov/index.aspx?nid=4836',
    notes='This data was requested via email.',    
    name_func=processing.simple_index_namer(['DISTRICT']),
    id_func=processing.simple_index_namer(['DISTRICT']),
    slug_func=processing.simple_index_namer(['DISTRICT']), 
)
boundaries.register('St. Paul District Councils (2014)',
    file='neighborhoods/2014-st-paul-district-councils/',
    last_updated=date(2013, 6, 4),
    name='St. Paul District Councils (2014)',
    singular='St. Paul District Council (2014)',
    domain='Minnesota',
    authority='City of St. Paul',
    source_url='http://stpaul.gov/index.aspx?nid=4836',
    notes='This data was requested via email.',
    name_func=processing.simple_index_namer(['DISTRICT']),
    id_func=processing.simple_index_namer(['DISTRICT']),
    slug_func=processing.simple_index_namer(['DISTRICT']), 
)

# MetCouncil districts
boundaries.register('Metropolitan Council districts (2013)',
    file='metropolitan-council-districts/',
    last_updated=date(2013, 10, 10),
    name='Metropolitan Council districts (2013)',
    singular='Metropolitan Council district (2013)',
    domain='Minnesota',
    authority='MN State Legislature',
    source_url='http://www.gis.leg.mn/html/download.html',
    notes='',
    name_func=processing.simple_index_namer(['district']),
    id_func=processing.simple_index_namer(['id']),
    slug_func=processing.simple_index_namer(['district']), 
)

# Minneapolis Parks and Recreation districts
boundaries.register('Minneapolis Parks and Recreation districts (2012)',
    file='parks-recreation-districts/2012-minneapolis-parks-recreation/',
    last_updated=date(2013, 10, 17),
    name='Minneapolis Parks and Recreation districts (2012)',
    singular='Minneapolis Parks and Recreation district (2012)',
    domain='Minnesota',
    authority='Minneapolis Parks and Recreation Board',
    source_url='http://www.minneapolisparks.org/default.asp?PageID=1005',
    notes='Recieved via email from the Minneapolis Parks and Recreation Board.',
    name_func=processing.simple_index_namer(['mplspark']),
    id_func=processing.simple_index_namer(['mplspark']),
    slug_func=processing.simple_index_namer(['mplspark']), 
)
boundaries.register('Minneapolis Parks and Recreation districts (2014)',
    file='parks-recreation-districts/2014-minneapolis-parks-recreation/',
    last_updated=date(2013, 10, 17),
    name='Minneapolis Parks and Recreation districts (2014)',
    singular='Minneapolis Parks and Recreation district (2014)',
    domain='Minnesota',
    authority='Minneapolis Parks and Recreation Board',
    source_url='http://www.minneapolisparks.org/default.asp?PageID=1005',
    notes='Compiled manually from multiple shapefiles recieved via email from the Minneapolis Parks and Recreation Board.',
    name_func=processing.simple_index_namer(['id']),
    id_func=processing.simple_index_namer(['id']),
    slug_func=processing.simple_index_namer(['id']), 
)
boundaries.register('Minneapolis Parks and Recreation districts (2022)',
    file='parks-recreation-districts/minneapolis-park-board-districts-2022/',
    last_updated=date(2022, 3, 3),
    name='Minneapolis Parks and Recreation districts (2022)',
    singular='Minneapolis Parks and Recreation district (2022)',
    domain='Minnesota',
    authority='Minneapolis Charter Commission',
    source_url='https://www.minneapolismn.gov/government/programs-initiatives/redistricting/',
    notes='Shapefiles downloaded from redistrictr of final plans from city redistricting group',
    name_func=boundaries.attr('districtr'),
    id_func=boundaries.attr('districtr'),
    slug_func=boundaries.attr('districtr')
)

boundaries.register('Minnesota State (2014)',
    file='state-mn/2014-mndot/',
    last_updated=date(2014, 7, 30),
    name='Minnesota State (2014)',
    singular='Minnesota State (2014)',
    domain='Minnesota',
    authority='Minnesota Department of Transportation',
    source_url='http://www.dot.state.mn.us/maps/gdma/gis-data.html',
    notes='Manually reprojected with ogr2ogr mn-state.shp state.shp -s_srs EPSG:26915 -t_srs EPSG:4326',
    name_func=processing.simple_index_namer(['STATE_FIPS']),
    id_func=processing.simple_index_namer(['STATE_FIPS']),
    slug_func=processing.simple_index_namer(['STATE_FIPS']), 
)
