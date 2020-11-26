# -*- coding: utf-8 -*-
# Proyecto que consiste en crear un programa que simule una caja registradora
# Cada vez que ejecutamos el programa, este probara su funcionalidad a travÃ©s de unittest
# El programa no tiene interfase grÃ¡fica

import sys
import unittest

# 
class Registradora(object):

    codigos = [101, 102, 103, 104, 105]
    precios = [14.00, 16.00, 18.00, 12.00, 15.00]
    descuentos = [0.10, 0.15, 0.12, 0.10, 0.15]

    def __init__(self):
        self._ticketCompra=[]
        self._totalCompra=0.00
        self._totalDescuento=0.00
        self._totalCambio=0.00
        self._numartTicket=0
        self._totalPagar=0.00

    def scan_product(self, n):
        productTicket=False
        for i in range(len(self.codigos)):
            if self.codigos[i] == n:
                self._totalCompra=self._totalCompra+self.precios[i]
                self._totalDescuento=self._totalDescuento+self.precios[i]*self.descuentos[i]
                self._totalPagar=self._totalPagar+(self.precios[i]-self.precios[i]*self.descuentos[i])
                self._ticketCompra.append(n)
                self._numartTicket= self._numartTicket+1
                productTicket = True
        return productTicket
    
    def gettotalCompra(self):
        return self._totalCompra

    def gettotalDescuento(self):
        return self._totalDescuento

    def getticketCompra(self):
        return self._ticketCompra

    def getnumartTicket(self):
        return self._numartTicket

    def gettotalPagar(self):
        return self._totalPagar
                
        

class RegistradoraTest(unittest.TestCase):
   
    def setUp(self):
        self.register = Registradora()

    def test_one_registradora(self):
        resultScan = self.register.scan_product(101)
        self.assertTrue(resultScan)

    def test_two_registradora(self):
        resultScan = self.register.scan_product(102)
        self.assertTrue(resultScan)

    def test_three_registradora(self):
        resultScan = self.register.scan_product(103)
        self.assertTrue(resultScan)

    def test_four_registradora(self):
        resultScan = self.register.scan_product(120)
        self.assertFalse(resultScan)

    def test_five_registradora(self):
        self.register._totalCompra = 48.0
        totala = self.register.gettotalCompra()
        self.assertEqual(48.00, totala)

    def test_six_registradora(self):
        self.register._totalDescuento = 5.96
        totalb = self.register.gettotalDescuento()
        self.assertEqual(5.96, totalb)

    def test_seven_registradora(self):
        self.register._numartTicket = 3
        totalc = self.register.getnumartTicket()
        self.assertEqual(3, totalc)

    def test_eigth_registradora(self):
        self.register._totalPagar = 42.04
        totald = self.register.gettotalPagar()
        self.assertEqual(42.04, totald)

    def test_nine_registradora(self):
        self.register._ticketCompra = [101,102,103]
        ticket = self.register.getticketCompra()
        self.assertListEqual([101,102,103], ticket)

if __name__ == '__main__':
    unittest.main()