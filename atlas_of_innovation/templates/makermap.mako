<!DOCTYPE html>
<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=Libre+Baskerville|Source+Sans+Pro:200,300,300i,400,600" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="${request.static_url('atlas_of_innovation:static/css/leaflet.css')}" />
    <link rel="stylesheet" type="text/css" href="${request.static_url('atlas_of_innovation:static/css/MarkerCluster.css')}" />
    <link rel="stylesheet" type="text/css" href="${request.static_url('atlas_of_innovation:static/css/MarkerCluster.Default.css')}" />
    <link rel="stylesheet" type="text/css" href="${request.static_url('atlas_of_innovation:static/css/stylesheet.css')}" />
    <script type='text/javascript' src="${request.static_url('atlas_of_innovation:static/js/leaflet.js')}"></script>
	<script type='text/javascript' src='${request.static_url('atlas_of_innovation:static/js/leaflet.markercluster.js')}'></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script type='text/javascript' src="${request.static_url('atlas_of_innovation:static/js/page.js')}"></script>
    <title>Ananse Innovation Map</title>
</head>
<body>

    <%include file="snippets/header.mako" />

    <div id="map-page-title-container">
    	<h1 id="map-page-title">Crowdsourced Atlas of Community Innovation Spaces</h1>
    </div>
    <div id="map-container">
	    <div id="map"></div>
        <div id="loading">
            <div class="loader"></div>
            <h3 class="loader-text">Finding Spaces...</h3>
        </div>
    </div>
    <div id="filter-bar">
        <div id="filters">
            <ul id="type-filter" class="filter-menu">
                % for type in ("All", "Workshop","Hub", "Event", "Ecovillage", "Virtual"):
                    <li>
                        <a href="#" class="filter-item" data-filter-group="types" data-filter-item="${type.lower()}">
                            <div class="filter-type-color ${type.lower()}-color"></div>
                            % if type == 'Workshop' :
                                Workshops
                            % elif type == 'Hub' :
                                Hubs
                            % elif type == 'Virtual' :
                                Virtual Spaces 
                            % elif type == 'All' :
                                All
                            % else :
                                ${type +'s'}                                
                            % endif
                        </a>
                    </li>
                % endfor
            </ul>
            <ul id="theme-filter" class="filter-menu">
                % for theme in ('Agriculture', 'Appropriate Technology', 'Art and Culture','Biology', 'Design', 'Education','Youth', 'Science', 'Education', 'Food', 'Materials', 'Media', 'Politics'):
                    <li>
                        <span class="filter-type-color agriculture-color"></span>
			<a href="#" class="filter-item" data-filter-group="theme" data-filter-item="${theme.lower()}">${theme}</a>
                    </li>
                %endfor        
            </ul>
        </div>
        <div class="filter-buttons">
            % for a in ("Type", "Theme"):
                <a href="/" id="filter-bar-type-button" class="filter-bar-button" data-filter="${a.lower()}">
                    <span class="filter-button-text">${a}</span>
                    <img src="${request.static_url('atlas_of_innovation:static/images/plus.png')}" class="filter-button-plus">
                    <img src="${request.static_url('atlas_of_innovation:static/images/minus.png')}" class="filter-button-minus">
                </a>
            % endfor
        </div>
        <a id="sponsor-giz" href="http://www.bmz.de/en/index.html" target="_blank">
            <img src="${request.static_url('atlas_of_innovation:static/images/giz-logo.png')}">
        </a>    

	</div>    
    <div id="info-bar">
       <h5 class="header">We sourced information from different databases and likely have many mistakes– please make corrections! Thanks to the <a href="http://www.bmz.de/en/index.html" target="_blank">German Ministry for Economic Cooperation and Development (BMZ)</a>, as well as our other sponsors and mapping partners.</h5>
        <!-- <ul class="sponsors">
            <li class="large">
                <a href="https://www.giz.de/" target="_blank">
                    <img src="/assets/sponsors/giz.png">
                </a>
            </li>
            <li>
                <a href="https://www.fabfoundation.org/" target="_blank">
                    <img src="/assets/sponsors/fab-foundation.png">
                </a>
            </li>
            <li>
                <a href="https://www.asme.org/" target="_blank">
                    <img src="/assets/sponsors/asme.png">
                </a>
            </li>
            <li>
                <a href="http://bongohive.co.zm/" target="_blank">
                    <img src="/assets/sponsors/bongohive.png">
                </a>
            </li>
            <li>
                <a href="http://www.globalinnovationgathering.com/" target="_blank">
                    <img src="/assets/sponsors/gig.png">
                </a>
            </li>
            <li>
                <a href="http://hacedores.com/" target="_blank">
                    <img src="/assets/sponsors/hacedores.png">
                </a>
            </li>
            <li>
                <a href="http://hackerspaces.org" target="_blank">
                    <img src="/assets/sponsors/hackerspaces.png">
                </a>
            </li>
            <li>
                <a href="http://www.instructables.com" target="_blank">
                    <img src="/assets/sponsors/instructables.png">
                </a>
            </li>
            <li>
                <a href="http://makermedia.com/" target="_blank">
                    <img src="/assets/sponsors/maker-media.png">
                </a>
            </li>
            <li>
                <a href="http://www.makery.info/" target="_blank">
                    <img src="/assets/sponsors/makery.png">
                </a>
            </li>
            <li>
                <a href="http://www.nesta.org.uk" target="_blank">
                    <img src="/assets/sponsors/nesta.jpg">
                </a>
            </li>
            <li>
                <a href="http://superherospaces.com/" target="_blank">
                    <img src="/assets/sponsors/shs.png">
                </a>
            </li>
        </ul>  -->
        </div>
    <script type='text/javascript' src="${request.static_url('atlas_of_innovation:static/js/map.js')}"></script>
</body>
</html>
