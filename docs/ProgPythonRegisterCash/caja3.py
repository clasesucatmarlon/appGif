import unittest
import random

class CashRegister:

    list_product_price = [110,220,330,440,550,660,770,880,990,1010]     # valores pre-cargados de una caja registradora comun

    list_product = []
    list_product_code = []
    subtotal_price_list =[]


    def product_input(self,product,code):

        #####################################################################
        # Se encarga del almacenar los productos y sus codigos en una lista #
        #####################################################################

        self.list_product.append(product)
        self.list_product_code.append(code)

        subtotal = self.subtotal_calc()                                 # obtiene el valor del producto ingresado y 
                                                                        # lo almacena para luego calcular el total
        return self.list_product, self.list_product_code, subtotal 


    def subtotal_calc(self):    

        len_list_product = len(self.list_product)
        len_subtotal_price_list = len(self.subtotal_price_list)

        ############################################################################################
        # Si se llama a este metodo, sin haber ingresado un producto nuevo, el mismo reingresara   #
        # el valor del ultimo producto cargado, generando errores.                                 #
        # Para solucionar eso, al principio del programa se revisa si la lista de productos es     #
        # mayor a la de precios guardados. De ser un caso positivo significara que se ingreso un   #
        # nuevo producto y se debe agregar su valor a la pila. En caso que no sea asi (sera igual),# 
        # se identificara que no se ingreso un nuevo producto y retornara el valor del ultimo      #
        # producto ingresado.                                                                      #
        ############################################################################################

        if len_list_product > len_subtotal_price_list:

            code_product = self.list_product_code[-1] 
            subtotal =  self.list_product_price[(code_product -1)]
            
            self.subtotal_price_list.append(subtotal)       # guarda en una lista los valores 
                                                            # de cada producto ingresado
        else: subtotal = self.subtotal_price_list[-1]                                                    
        
        return subtotal


    def total_calc(self):

        ########################################################
        # Se calcula el valor total de la compra y ademas el   # 
        # descuento porcentual correspondiente a cada producto #
        ########################################################

        discount_list = []
        discount = 0
        r = 0

        total = sum(self.subtotal_price_list)

        for i in range(len(self.list_product)):
            n = random.randint (0, 3)                       # El procentaje de desceunto es aleatorio
                                                            # entre los valores de 0%, 10%, 20%, 30%
            discount_list.append(n*10)                  
            r = ((n*10)*self.list_product_price[i])/100   
            discount += r

        self.print_ticket(total, discount, discount_list)   # descomentar para visualizar el ticket

        return total, discount, discount_list               


    def print_ticket(self,total,discount,discount_list):


        ##########################################################
        # Este metodo solo sirve para imprimir todos los valores #
        # y resultados anteriormente calculados, por lo que no   #
        # raliza ningun calculo o operacion, as que imprimir en  #
        # pantalla; por esta razon no posee una funcion de tipo  #
        # test. En caso de querer probarlo, descomentar la       #
        # llamada a este metodo en el metodo anterior.           #
        ##########################################################

        print("\n--------------------------------------------")

        print('\n{:^10}{:^10}{:^10}{:^10}\n'.format("productos","codigo","precio","descuentos"))

        n = len(self.list_product)
        for i in range(n):
            print('{:^10}{:^10}{:^10}{:^10}'.format(self.list_product[i],self.list_product_code[i],'$ '+ str(self.list_product_price[i]),'-' + str(discount_list[i])+'%'))

        print("\n--------------------------------------------\n")
        print("Subtotal: {:>27}".format('$'+ str(total)))
        print("Total descuento: {:>21}\n".format('$'+ str(discount)))
        print("Total a cobrar:{:>23}".format("$"+ str(total - discount)))

        return True   

        
            


####################################################################################################################################

class CashRegisterTest(unittest.TestCase):

    def setUp(self):
        self.cash_register = CashRegister()
        self.number_product = 0
        self.code_list = [1,2,3,4,5,6,7,8,9,10]                  # al no ingresar cogido de barras por
                                                                 # teclado se pre-cargan valores ya definidos

    def test_A(self):

        ########################################################################
        #  El testeo esta planteado para que simule el ingreso de 3 productos, #
        #  y simule que el comprador no quiere seguir comprando.               #
        # Sin embargo, puede realizarlo las veces que se le indique cambiando  #
        # el valor de la variable "reps" (max 10)                              #                                              
        ########################################################################
        
        reps = 5

        while True:
            self.number_product +=1
            self.name_product = 'producto ' + str(self.number_product) 
            number_code_list = self.number_product - 1
            
            product, code, subtotal= self.cash_register.product_input(self.name_product,self.code_list[number_code_list])
                                                
            #print(subtotal)                                 #simularia el mensaje del sub total, 
                                                             #mientras se ingresa los productos.
            

            if self.number_product >= reps:                    #simula un do-while
                break
        
        self.assertTrue(product, self.name_product)
        self.assertTrue(code, number_code_list)
        self.assertEqual(self.number_product, reps)


    def test_B(self):

        #####################################################
        # Este metodo tiene como unica funcion verificar    #
        # o comprobar el correcto funcioanamineto del       # 
        # metodo "subTotal_calc",                           #
        # la simulacion de la imprecion del subtotal al     #
        # ingresar el producto lo realiza el metodo original#
        #####################################################

        subtotal = self.cash_register.subtotal_calc()  

        last_code =self.cash_register.list_product_code[-1]     
        self.assertEqual(subtotal, self.cash_register.list_product_price[last_code - 1])


    def test_C(self):
        
        #######################################################
        # al igual que el metodo anterior, este solo verifica #
        # el funcionamiento del metodo original               #
        #######################################################


        total, discount, discount_list= self.cash_register.total_calc()
        
        self.assertEqual(total,sum(self.cash_register.subtotal_price_list))
        len_list_product = len(self.cash_register.list_product)
        self.assertEqual(len(discount_list),len_list_product)
        self.assertLess(discount, total)
        



if __name__ == '__main__':
    unittest.main() 