import sys
import requests
import optparse
from tabulate import tabulate


#Sets URL to server
BASE_URL = 'http://127.0.0.1:8080'


# get a list of all nodes
def get_all_nodes():
    url = BASE_URL + '/nodes'

    response = requests.get(url)
    return response


# get data for a specific node
def get_node_data(node_name):
    url = BASE_URL + '/hostdata/' + node_name

    response = requests.get(url)
    return response


# get a list of all groups
def get_all_groups():
    url = BASE_URL + '/groups'

    response = requests.get(url)
    return response


# get all groups associated with a specific node
def get_all_groups_with_node(node_name):
    url = BASE_URL + '/nodes/' + group_name

    response = requests.get(url)
    return response


# get data (nodes) for a specific group
def get_group_data(group_name):
    url = BASE_URL + '/groups/' + group_name

    response = requests.get(url)
    return response


# Shows the total CPU, memory, and disk space of each group and allows us
# to limit to top-k results (invdb group-resources --limit 5)
def group_resources(limit=0, reverse=False):
    reverse = not reverse
    group_list = get_all_groups()
    group_data_list = []

    for group in group_list.json():
        nodes_in_group = get_group_data(group)

        total_cpu = 0
        total_memory = 0
        total_disk_space = 0

        for node in nodes_in_group.json():
            node_data = get_node_data(node).json()
            total_memory += node_data['memtotal_mb']

            total_cpu += calc_total_cpu(node_data)

            total_disk_space += calc_total_disk(node_data)

        group_data = {'Group Name': group, 'Memory (MB)': total_memory, 'CPU (GHz)': total_cpu, 'Disk Space (GB)': total_disk_space}
        group_data_list.append(group_data)

    group_data_list.sort(reverse=reverse, key=lambda x: x['Memory (MB)'])

    if limit > 0:
        print_group_data(group_data_list[:limit])
        return group_data_list[:limit]
    else:
        print_group_data(group_data_list)
        return group_data_list


def print_group_data(group_data):
    headers = ['Group Name', 'Memory (MB)', 'CPU (GHz)', 'Disk Space (GB)']
    rows = [x.values() for x in group_data]
    print(tabulate(rows, headers=headers))

# calculate the CPU of a given node (CPU * processor_count)
def calc_total_cpu(node_data):
    for processor in node_data['processor']:
        cpu = 0

        # extract the raw GHz number from the processor description string
        if 'GHz' in processor:
            processor_split = processor.split('@')
            if len(processor_split) > 1:
                processor = processor_split[1]
                cpu = float(processor.replace('GHz', '').replace(' ', ''))

    processor_count = node_data['processor_count']
    return cpu * float(processor_count)


def calc_total_disk(node_data):
    devices = node_data['devices']

    # space on this node in GB
    total_space_on_this_node = 0

    for key, value in devices.items():
        size = value.get('size', None)
        if not size:
            break
        size = size.split(' ')
        unit = size[1]
        number = size[0]

        #converted TB to GB if needed
        if unit == 'TB':
            number = float(number) * 1024
        elif unit == 'GB':
            number = float(number)
        else:
             number = 0

        total_space_on_this_node += number


    return total_space_on_this_node


def check_group_overlap(groups):
    prev_group_nodes = None
    overlap_nodes = []

    if len(groups) < 2:
       group_nodes = get_group_data(groups[0]).json()
       return group_nodes
    else:
        group_nodes1 = get_group_data(groups[0]).json()
        group_nodes2 = get_group_data(groups[1]).json()
        overlap_nodes = list(set(group_nodes1) & set(group_nodes2))

    for group in groups:
        group_nodes = get_group_data(group).json()

        if overlap_nodes:
            overlap_nodes = list(set(group_nodes) & set(overlap_nodes))

    overlap_nodes = list(set(overlap_nodes))
    print(overlap_nodes)
    return overlap_nodes


if __name__ == '__main__':
    args = sys.argv[1:]

    #Sets up optional arguments for CLA
    parser = optparse.OptionParser()
    parser.add_option('-l', '--limit', dest='limit', help='Limit', type=int)
    parser.add_option('-g', '--groups', dest='groups', help='Groups')
    parser.add_option('-r', '--reverse', dest='reverse', help='Reverse')

    (options, _) = parser.parse_args()

    limit = vars(options).get('limit', 0)
    reverse = vars(options).get('reverse', False)

    if 'group-overlap' in args:
        groups = vars(options).get('groups', '')

        groups = groups.split(',')

        check_group_overlap(groups)


    if 'group-resources' in args:
        if reverse:
            group_resources(limit, reverse=True)
        else:
            group_resources(limit)
