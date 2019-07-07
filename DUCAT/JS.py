import  json
data ={}
data['People'] = []
ans = 'y'
name = ''
Website = ''
From =''
while(ans):
    print('1.Wrting from the JSON File')
    print('2.Reading to the JSON File')
    print('3.Searching in a JSON File')
    print('4.Exit')
    val = int(input('Enter your choice: '))

    if val == 1:
        value = int(input('Enter the values:'))
        for x in range(value):
            name = input('Enter name')
            Website = input('Enter Website')
            From = input('Enter From')

            data['People'].append({
                'name ':name,
                'Website ': Website,
                'From' : From
            })


        with open('demo.json','a+') as file:
            json.dump(data,file)


    elif val == 2:
        with open('demo.json','r') as file:
            data = json.load(file)
            for p in data['People']:
                print('Name: ',p['name '])
                print('Website: ',p['Website '])
                print('From: ',p['From'])

    elif val == 3:
        with open('demo.json','r') as file:
            data = json.load(file)
        str = input('Enter name to search: ')
        for p in data['People']:
            if p['name '] == str:
                print('Name: ',p['name '])
                print('Website: ',p['Website '])
                print('From: ',p['From'])
            else:
                print('Not present')

    elif val == 4:
        exit(0)


    else:
        print('Wrong Choice')
        exit(0)

    ans = input('Continue y/n')