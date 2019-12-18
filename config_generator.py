from datetime import datetime
from jinja2 import Template
import csv
import logging

# main script
stamp=('{:%Y.%m.%d}'.format(datetime.now()))

try:
    logging.basicConfig(filename=datetime.now().strftime('logs/' + stamp + '.log'),
                        level=logging.DEBUG)  # for storing process log

    logging.info("Script ran at: " + stamp)

    with open("input/ReferenceTemplate.j2") as input_template:
        input_template_data = Template(input_template.read())

    with open("input/InputVariableSheet.csv") as input_csv:
        input_csv_data = csv.DictReader(input_csv)
        for row in input_csv_data:
            hostname = row["Hostname"]
            device_config = input_template_data.render(
                site_name = row["Site Name"],
                hostname = row["Hostname"],
                mgmt_ip_address = row["Mgmt IP Address"],
                pip_address = row["PIP Address"],
                sbn_mask = row["SBN Mask"],
                vrrp_ip = row["VRRP IP"],
                speed = row["Speed"],
                as_num = row["AS-Num"],
                local_subnet = row["Local Subnet"],
                wild_mask = row["Wild Mask"],
                next_hop = row["Next Hop"],
                wan_sbn = row["WAN-SBN"],
                wan_sm = row["WAN-SM"]

            )
            with open("output/" + hostname + ".txt","w") as f:
                f.write(device_config)

except Exception as e:
    print(str(e))
    logging.error("Error: " + str(e))
