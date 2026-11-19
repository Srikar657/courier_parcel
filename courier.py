
parcels = {}

def add_parcel(id, sender, receiver):
    parcels[id] = [sender, receiver, "Booked"]
    return "Parcel Added"

def track_parcel(id):
    if id in parcels:
        return parcels[id]
    return "Parcel Not Found"

def update_status(id, status):
    if id in parcels:
        parcels[id][2] = status
        return True
    return False

def delete_parcel(id):
    if id in parcels:
        del parcels[id]
        return True
    return False
