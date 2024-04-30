Design
======

This is a somewhat informal document on how I think OpenCallerDB should be designed.

Principles
----------

OpenCallerDB aims to be a crowdsourced database of caller information that is:

- Free and Open Source;
- Easy to use;
- Lightweight;
- (Somewhat) Federated;
- Exposing a simplistic API;
- Exposing a simple web interface;

Federating
----------

Federating will be done in a way that takes heavy inspiration from how DNS work.

Each server will have its own review database, as well as a list of other instances that can be queried when a certain phone number cannot be found inside the review database.

Each response that came from the "federated servers" will contain only the minimal amount of data to allow a user to be able to understand if a number is safe or dangerous: this means that reviews will not be transferred between servers, but only the number of positive, negative and neutral reviews, as well as the "most selected" type.

Querying
--------

### Via API

Each API request on a federated server will do the following:

1. Check the local reviews, if any are present, return the following information:
    - Number of positive reviews;
    - Number of negative reviews;
    - Number of neutral reviews;
    - Most common category chosen by the reviewers;
2. If there are no reviews in the local DB, check the federated cache, if there is a cache hit, return the information contained therein.
3. If there are no hits from the local review DB, query the federated servers (which servers to query will be saved in a database table). The federated servers will return the minimal information as in point 1 and save them in the local cache.
4. If none of the federated server finds the number, return a negative response.

### Via Web Interface

Each API request on a federated server will do the following:

1. Check the local reviews, if any are present, show them on screen.
2. If there are no reviews available, check the federated cache, if there is a cache hit, return the following information:
    - Number of positive reviews;
    - Number of negative reviews;
    - Number of neutral reviews;
    - Most common category chosen by the reviewers;
    - Link to the federated server for more information;
3. If there are no hits from the local review DB, query the federated servers (which servers to query will be saved in a database table). The federated servers will return the minimal information as in point 2 and save them in the local cache.
4. If none of the federated server finds the number, return a negative response.
