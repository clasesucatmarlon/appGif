import unittest  # Módulo para realizar las pruebas
import random # Para usar la funcion aleatoria

class RegisterCash:
    """  Clase para caja registradora
    """
    productPrice = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]    

    product = []
    productCode = []
    priceSubtotal =[]


    def productInput(self, product, code):
        """ Método para capturar y guardar productos y códigos
        """
        self.product.append(product)
        self.productCode.append(code)
        subtotal = self.subtotalCalc()
        return self.product, self.productCode, subtotal 


    def subtotalCalc(self):    
        """ Método para calcular el subtotal
        """
        countProduct = len(self.product)
        countSubtotal = len(self.priceSubtotal)
        if countProduct > countSubtotal:
            code_product = self.productCode[-1] 
            subtotal =  self.productPrice[(code_product -1)]          
            self.priceSubtotal.append(subtotal)
        else: subtotal = self.priceSubtotal[-1]                                                    
        return subtotal


    def calcTotal(self):
        """ Método para el calculo de la compra total
        """
        discList = []
        disc = 0
        r = 0
        total = sum(self.priceSubtotal)
        for i in range(len(self.product)):
            n = random.randint (0, 3)
            discList.append(n*10)                  
            r = ((n*10)*self.productPrice[i])/100   
            disc = disc + r
        self.print_ticket(total, disc, discList)
        return total, disc, discList               


    def print_ticket(self,total,disc,discList):
        """ Método para imprimir
        """
        print('\n{:^10}{:^10}{:^10}{:^10}'.format("products","code","price","discount"))
        print("-" * 42)
        n = len(self.product)
        for i in range(n):
            print('{:^10}{:^10}{:^10}{:^10}'.format(self.product[i],self.productCode[i],'$ '+ str(self.productPrice[i]),'-' + str(discList[i])+'%'))

        print("-" * 42)
        print("Subtotal: {:>27}".format('$'+ str(total)))
        print("Total discount: {:>23}".format('$'+ str(disc)))
        print("Total to charge:{:>23}".format("$"+ str(total - disc)))
        return True   


# TEST
class CashRegisterTest(unittest.TestCase):
    """ Test caja registradora
    """
    def setUp(self):
        """ Carga inicial
        """
        self.cRegistrer = RegisterCash()
        self.nProduct = 0
        self.lCode = [1,2,3,4,5,6,7,8,9,10]

    def testFirst(self):
        """ Primer test
        """
        reps = 5

        while True:
            self.nProduct += 1
            self.nameProduct = 'Product ' + str(self.nProduct) 
            numlCode = self.nProduct - 1
            product, code, subtotal= self.cRegistrer.productInput(self.nameProduct,self.lCode[numlCode])
            if self.nProduct >= reps:
                break
        self.assertTrue(product, self.nameProduct)
        self.assertTrue(code, numlCode)
        self.assertEqual(self.nProduct, reps)


    def testSecond(self):
        """ Segundo test
        """
        subtotal = self.cRegistrer.subtotalCalc()  
        lastCode = self.cRegistrer.productCode[-1]     
        self.assertEqual(subtotal, self.cRegistrer.productPrice[lastCode - 1])


    def testThirt(self):
        """ Tercer test
        """
        total, disc, discList = self.cRegistrer.calcTotal()
        self.assertEqual(total,sum(self.cRegistrer.priceSubtotal))
        countProduct = len(self.cRegistrer.product)
        self.assertEqual(len(discList),countProduct)
        self.assertLess(disc, total)


if __name__ == '__main__':
    unittest.main() 