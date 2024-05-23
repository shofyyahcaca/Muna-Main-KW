# Summary Documentation Muna System
## requirement analysis 
### Muna Main
* The root base of all the parts of systems, for instance, schedule, dashboard, data manager, and auth system
* Manage API in each module and service
* Manage to create, read, update, and delete database
* The established code base uses the concept of clean code architecture and design pattern

### Muna Auth
* Registration member munaqasah
* Login munaqasah system
* Authentication and authorization of an account to log in and log out and also the process of registration
* Manage standard auth system based on OAuth 2.0
* User role of four account levels, for instances
  * Super Admin (Founder) can access all function
  * Developer (Founder & Developer) access feature is still being developed, and the source code base.
  * Manager (Kepala Jurusan & Sekretaris Jurusan) 
    * Manage schedule munaqasah
    * Change the lecture as the examiner
    * Move supervisor to another schedule
    * Canceling scheduled munaqasah
  * Operator (Tenaga Pendidik) 
    * Manage schedule munaqasah manually
    * Manage schedule munaqasah based on the recommendation of the system
    * Editing the schedule munaqasah based on notes from the manager or problems with the schedule
  * Member Munaqasah (Mahasiswa) 
    * Member Register
    * Data Entry Name & Nim to triggering data Master Students from Sinau

### Muna Mobile
* Login & Registration munaqasah
* Get & Push API from the server or main server
* Feed schedule munaqasah
* Report that the lecturer cannot be the examiner
* Reminder of the schedule munaqasah based on notification

### Muna Data Manager
* Scraping data students, lecturer, schedule teaching lecture when Tendik is opening Sinau
* Read data historical from historical data munaqasah
* Checklist data completed by students is not missing or null after scraping
* The operator can control whether data is good quality or not based on scraping is not complete

### Muna Dashboard
* Show data statistic member munaqasah new and old
* Show probabilistic spare time lecturer for scheduled munaqasah based on master data lecturer and scheduled teaching.
* Show reporting lecturer still does not have time to be the examiner
* All the data gets directly from the database's slow response, and memory uses the cache to get a faster response

### Muna Schedule
* Operator and Manager able to manage munaqasah manually
* The system can give recommendations based on historical munaqasah before
* The operator and Manager can see dropdown lecturer, time, day, and room and choose a thesis based on cluster knowledge
* The operator and Manager can select each item to schedule munaqasah
* The system can give a warning the schedule munaqasah is not suitable, for instance, time, room, and day, or the lecturer does not have time to teach


# Concepts
this system use two design pattern for instance, [Facade Pattern](https://refactoring.guru/design-patterns/facade) implemented into the system & the subsystem for instances API relate to Database. and inside of subsystem will use [Observer Pattern](https://refactoring.guru/design-patterns/observer) for control the data update from subsystem into database, for instances notified, new data or update data.

# features (other features can be analyzed again based on documentation and explanation by lecturer in classroom) 

## Muna Main
### Core (System)
* controller services
* controller orm

### Application Programming Interface (Subsystem)
* auth services
* lecturer feeder services
* course feeder services
* students feeder services
* schedule historical services
* scheduling services

### Database (Object Relation Model) (other attribute table can be analyzed again based on documentation and explanation by lecturer in classroom)
* auth: nim, nip, salt+nim+password+platfrom, type platform
* lecturers database: name, nip,
* course database: name course, day, start time, end time, name lecturer
* students database: name, nim, prodi, masuk tahun, status, semester, IPK lulus
* item munaqasah: name, nim, judul, status, link data munaqasah
* data detail munaqasah: id item munaqasah, name dosen pembimbing 1
* data syarat ujian (storage link pdf): berkas tugas akhir, SKEK, herregistrasi, KRS, plagiasi, lulus semua mata kuliah, sertifikat IBI, IBA, sertifikat P2KKM, sertifikat ICT, ijazah terakhir, sertifikat P2KBTA-KKP
* schedule munaqasah: name lecturer1, lecturer2, lecturer3, name students, datetime, room
* historical munaqasah: schedule munaqasah, datetime, periode, year
* report munaqasah: name lecturer, nip, count exam, name students