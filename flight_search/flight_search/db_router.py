class MasterReplicaRouter:
    def db_for_read(self, model, **hints):
        # return 'replica' to be used once we have set up the replication from master db
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True  # Allow relations between both DBs

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'  # Only run migrations on master
