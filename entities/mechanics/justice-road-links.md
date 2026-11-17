---
id: justice-road-links
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/justice-courts-prisons-design.md
- entities/mechanics/travel-routes.md
- entities/locations/route-ashvale-eastrun.md
- entities/locations/route-eastrun-briarfall.md
- entities/locations/route-waystation-brackenford.md
- entities/locations/route-brackenford-cottage.md
- entities/locations/route-caelthorne-ashvale-estate.md
- entities/locations/route-caelthorne-eastrun.md
- entities/locations/route-caelthorne-briarfall-crossing.md
- entities/locations/route-caelthorne-blackthorn-watch.md
- entities/locations/route-caelthorne-ironhollow-hold.md
- entities/locations/route-caelthorne-rivermere.md
- entities/locations/route-caelthorne-frostspire-peaks.md
- entities/locations/route-ashvale-estate-ashvale-lodge.md
- entities/locations/route-eastrun-greyhaven-mill.md
- entities/locations/route-eastrun-greyhaven-valley.md
- entities/locations/route-blackthorn-watch-blackthorn-north-waystation.md
- entities/locations/route-caelthorne-mount-vaelspire.md
- entities/locations/route-caelthorne-elyndor.md
- entities/locations/route-caelthorne-frostmarch.md
---

# Road jurisdiction lookup

All18 existing route owners are referenced without editing or promoting them. Endpoint public authorities are potential contacts at that endpoint, not verified corridor patrols or lawful receiving stations. No known precise patrol jurisdiction is supplied by the current road records; jurisdiction, nearest station, court and remand fields therefore remain null. No distance ranking from proximity, new border, cross-border agreement or prisoner transport is inferred.

```json
{
  "schema_version": 1,
  "roads": [
    {
      "route_id": "route-ashvale-eastrun",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "ashvale-estate",
          "authority_id": "justice:ashvale-private-security"
        }
      ],
      "source_refs": [
        "entities/locations/route-ashvale-eastrun.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-eastrun-briarfall",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [],
      "source_refs": [
        "entities/locations/route-eastrun-briarfall.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-waystation-brackenford",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "brackenford",
          "authority_id": "justice:brackenford-government"
        },
        {
          "location_id": "brackenford",
          "authority_id": "justice:brackenford-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-waystation-brackenford.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-brackenford-cottage",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "brackenford",
          "authority_id": "justice:brackenford-government"
        },
        {
          "location_id": "brackenford",
          "authority_id": "justice:brackenford-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-brackenford-cottage.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-ashvale-estate",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        },
        {
          "location_id": "ashvale-estate",
          "authority_id": "justice:ashvale-private-security"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-ashvale-estate.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-eastrun",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-eastrun.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-briarfall-crossing",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-briarfall-crossing.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-blackthorn-watch",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        },
        {
          "location_id": "blackthorn-watch",
          "authority_id": "justice:blackthorn-command"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-blackthorn-watch.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-ironhollow-hold",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-ironhollow-hold.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-rivermere",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-rivermere.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-frostspire-peaks",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-frostspire-peaks.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-ashvale-estate-ashvale-lodge",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "ashvale-estate",
          "authority_id": "justice:ashvale-private-security"
        }
      ],
      "source_refs": [
        "entities/locations/route-ashvale-estate-ashvale-lodge.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-eastrun-greyhaven-mill",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [],
      "source_refs": [
        "entities/locations/route-eastrun-greyhaven-mill.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-eastrun-greyhaven-valley",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [],
      "source_refs": [
        "entities/locations/route-eastrun-greyhaven-valley.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-blackthorn-watch-blackthorn-north-waystation",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "blackthorn-watch",
          "authority_id": "justice:blackthorn-command"
        }
      ],
      "source_refs": [
        "entities/locations/route-blackthorn-watch-blackthorn-north-waystation.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-mount-vaelspire",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-mount-vaelspire.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-elyndor",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-elyndor.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    },
    {
      "route_id": "route-caelthorne-frostmarch",
      "region_id": null,
      "responsible_authority_id": null,
      "nearest_station_location_id": null,
      "court_authority_id": null,
      "remand_facility_id": null,
      "endpoint_contacts": [
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-magistrates"
        },
        {
          "location_id": "caelthorne",
          "authority_id": "justice:caelthorne-watch"
        }
      ],
      "source_refs": [
        "entities/locations/route-caelthorne-frostmarch.md"
      ],
      "note": "Endpoint contacts only; route boundary, patrol coverage, receiving facility and distance-ranked station UNKNOWN. Read classification and access from route owner. No automatic transport."
    }
  ],
  "automatic_transport": false
}
```
