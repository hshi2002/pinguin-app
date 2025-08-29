const dbh = db.getSiblingDB("pinguin");
dbh.objects.createIndex({ next_due: 1 });
dbh.objects.createIndex({ host: 1 }, { unique: false });
