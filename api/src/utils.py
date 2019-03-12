def row_to_dict(row):
    res = {}
    for col in row.__table__.columns:
        if getattr(row, col.name):
            res.update({col.name: str(getattr(row, col.name))})
    return res
