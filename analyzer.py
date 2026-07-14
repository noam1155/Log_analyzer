
from checks import is_external, is_sensitive_port




def external_ips(all_lines:list) -> list:
    return [line[1] for line in all_lines if is_external(line[1]) ]



def sensitive_port(all_lines:list) -> list :
    return [line for line in all_lines if is_sensitive_port(line[3])]


def large_data(all_lines:list) -> list:
    return [line for line in all_lines if int(line[5]) >= 5000 ]


def tag_large_data(all_lines:list) :
    return [line + ["NORMAL"] if int(line[5]) < 5000 else line + ["LARGE"] for line in all_lines]

