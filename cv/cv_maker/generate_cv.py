from datetime import datetime
import logging
from weasyprint import HTML, CSS

level = logging.DEBUG

logger = logging.getLogger(__name__)
logger.setLevel(level)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s:  %(message)s')
ch.setFormatter(formatter)
ch.setLevel(level=level)
logger.addHandler(ch)


root_dir = "/home/maker/cv_maker/"

date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

html_file = f"{root_dir}html_css/cv.html"
output_pdf = f"{root_dir}output/cv_{date_time}.pdf"
css_file = f"{root_dir}html_css/page.css"


html_file = HTML(html_file)
css_file = CSS(f"{root_dir}html_css/page.css")

logger.info(f"Making CV from {html_file}.")

html_file.write_pdf(output_pdf)
html_file.write_pdf(f"{root_dir}output/cv.pdf")

logger.info(f"Ouput CV to {output_pdf}.")

