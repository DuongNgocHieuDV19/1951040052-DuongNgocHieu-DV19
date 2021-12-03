# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:04:07 2021

@author: DUONG NGOC HIEU
"""

SELECT a.cust_name AS "Customer Name", 
a.city, b.name AS "Salesman", 
b.commission FROM customer a INNER JOIN salesman b ON a.salesman_id=b.salesman_id;