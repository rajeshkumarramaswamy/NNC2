from django.shortcuts import render
from models import *
import json

def index(request):
	records = noc.objects.all()
	partner_records = partner.objects.all()
	client_records = client.objects.all()
	output = []
	partner_output = []
	client_output = []

	for record in records:
		noc_id = record.id
		noc_name = record.name
		output.append(noc_name)

	for pr in partner_records:
		pr_id = pr.id
		pr_name = pr.name
		partner_output.append(pr_name)

	for cl in client_records:
		cl_id = cl.id
		cl_name = cl.name
		client_output.append(cl.name)

	noc_data = []
	partner_data = []
	client_data = []
	
	noc_partner = {}
	noc_client = {}
	partner_client = {}
	
	for nc in records:
		noc_data.append((nc.id, nc.name))
		noc_partner.setdefault(str(nc.name), [])
		noc_client.setdefault(str(nc.name), [])
		p_records = partner.objects.filter(noc_id=nc.id)

		for p_r in p_records:
			partner_data.append((p_r.id, nc.id, p_r.name))
			noc_partner[str(nc.name)].append(str(p_r.name))
		
			partner_client.setdefault(str(p_r.name), [])	
			cl_records = client.objects.filter(noc_id=nc.id, partner_id=p_r.id)
			for c_r in  cl_records:
				client_data.append((c_r.id, nc.id, p_r.id, c_r.name))
				noc_client[str(nc.name)].append(str(c_r.name))
				partner_client[str(p_r.name)].append(str(c_r.name))

	print '****noc*******' 
	print noc_data
	print '*****partner******' 
	print partner_data
	print '******client*******'
	print client_data
		
        return render(request, 'index.html', {'output': output, 
		'noc_data': noc_data, 'partner_data': partner_data, 'client_data': client_data, 'partner_client': partner_client,
		'partner_output' : partner_output, 'client_output' : client_output, 'noc_partner': noc_partner, 'noc_client': noc_client})

