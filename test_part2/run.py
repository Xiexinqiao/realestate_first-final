# run.py
import coverage
import pytest
cov = coverage.coverage()
cov.start()
pytest.main(["-v", "-s"])
cov.stop()
cov.save()
cov.report()
cov.html_report(directory="res_html")