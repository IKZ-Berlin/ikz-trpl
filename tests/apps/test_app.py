def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from ikz_trpl.apps import app_entry_point

    assert app_entry_point.app.label == 'NewApp'