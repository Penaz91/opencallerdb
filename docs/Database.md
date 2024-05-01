Database Design
===============

Being software that is meant to be running on many small instances, the database should be space-efficient, while still giving enough capabilities for defining how a caller is identified.

Tables
------

### Review

| Field        | Type        | Flags              | Description                                                     |
| ------------ | ----------- | ------------------ | --------------------------------------------------------------- |
| Id           | Long        | PK, Auto-increment | Numeric Primary Key                                             |
| Number       | Long        | Index              | Phone number, with country code (without the + symbol)          |
| Evaluation   | Enum        |                    | Whether this number is safe, neutral or dangerous               |
| Category     | Enum        |                    | The category this number is part of, according to the review.   |
| Title        | Char(128)   |                    | A short description                                             |
| Detail       | Text        |                    | A detailed description of the experience with this number       |

The phone number will be memorized as an integer, by using some quirks guaranteed by the country code:

- There is no country code "zero", this means that we don't need to store the phone number as text
- Text is hard to index and search through. Integers are easy to index and can be queried in O(log(n)) via binary search on average.

Also the "Evaluation" and "Category" fields will be limited heavily to save on space:

- Evaluation will be stored as an Enum/SmallInteger, this limits the space occupied by each row.
- Category will be stored as an Enum/SmallInteger, this will limit the number of available categories to the necessary ones, also helping to save space.

### Federated Cache

| Field                 | Type        | Flags              | Description                                                             |
| --------------------- | ----------- | ------------------ | ----------------------------------------------------------------------- |
| Id                    | Long        | PK, Auto-increment | Numeric primary key                                                     |
| Number                | Long        | Unique?, Index     | Phone number, with country code (without the + symbol)                  |
| Category              | Enum        |                    | The category this number is part of, according to the federated server. |
| Positive Review No.   | Integer     |                    | The number of positive reviews                                          |
| Negative Review No.   | Integer     |                    | The number of negative reviews                                          |
| Neutral Review No.    | Integer     |                    | The number of neutral reviews                                           |
| Federated Server      | Integer     | FK                 | The link to the federated server for more information                   |
| Expiry                | DateTime    |                    | Date and time this cache row will expire and should be renewed          |

Having the federated server as a Foreign Key makes "Defederating" easier, since we can program a cascade deletion when we remove an URL from the federated servers table.

### Federated Servers

| Field   | Type         | Flags              | Description                                                                            |
| ------- | ------------ | ------------------ | -------------------------------------------------------------------------------------- |
| Id      | Long         | PK, Auto-increment | Numeric primary key                                                                    |
| URL     | Char(1024)   | Unique             | The URL to the Server we want to federate with                                         |
| TTL     | Integer      |                    | Number of seconds the results of the federated server should stay in our local cache   |
