from gerador import *
import gtk, gtk.glade
import pygtk
import gobject

class Janela ():
    arvore = None
    janela = None
    janela_salvar = None
    barra = None
    botao_gera = None
    botao_salva = None
    times = None
    texto_explicativo = None
    
    def __init__ (self):
        self.arvore = gtk.glade.XML ('window.glade')
        self.janela = self.arvore.get_widget ('window1')
        self.barra = self.arvore.get_widget ('toolbar1')
        self.botao_gera = self.arvore.get_widget ('toolbutton1')
        self.botao_salva = self.arvore.get_widget ('toolbutton2')
        self.times = self.arvore.get_widget ('textview1')
        buff = self.times.get_buffer ()
        buff.set_text ("Insira aqui os nomes dos times")
        self.texto_explicativo = True
        self.times.set_buffer (buff)
        
        self.janela.set_title ("Gerador de Tabelas")
        self.janela.show_all ()
        self.janela_salvar = self.arvore.get_widget ('filechooserdialog1')
        self.janela_salvar.set_title ("Salvar")
        self.arvore.signal_autoconnect (self)

    def quit (self, widget, data):
        gtk.main_quit ()
        
    def foca_texto (self, widget, data):
        if self.texto_explicativo:
            buff = self.times.get_buffer ()
            buff.set_text ("")
            self.times.set_buffer (buff)
            self.texto_explicativo = False
        
    def gera_clicked (self, widget):
        texto = self.times.get_buffer ()
        iter_inicio = texto.get_start_iter ()
        iter_fim = texto.get_end_iter ()
        lista_times = texto.get_text (iter_inicio, iter_fim).split ('\n')
        lista_times = valida_lista (lista_times)        
        num_times = len (lista_times)        
        
        if  num_times > 1:
            tabela = espalha (lista_times)
    
            self.tabela_final = "Tabela Gerada\n"
            self.tabela_final += "Numero de Times: " + str (len (lista_times)) + "\n"
            self.tabela_final += "Rodadas: " + str (2 * len (tabela[0])) + "\n\n"
            self.tabela_final += "Times: \n"
    
            for cada in lista_times:
                self.tabela_final += cada + "\n"
    
            self.tabela_final += "\n\n"        
            i = 1
            for turno in tabela:
                for rodada in turno:
                    self.tabela_final += "Rodada " + str (i) + "\n" + str (rodada) + "\n"
                    i += 1
            
            texto.set_text (self.tabela_final)
            self.times.set_buffer (texto)

        elif num_times == 1 and lista_times[0] == "5h20":
            texto.set_text ("Uh! Impulso, neh iss???")
        else:            
            texto.set_text ("Du'h!!! Soh com um time nao da!")

    def salva_clicked (self, widget):
        self.janela_salvar.show_all ()
    
    def ok_salva_clicked (self, widget):
        uri = self.janela_salvar.get_filename ()
        self.janela_salvar.hide ()
        arquivo = open (uri, 'w')
        arquivo.write (self.tabela_final)
        arquivo.close ()

    def cancela_salva_clicked (self, widget):
        self.janela_salvar.hide ()


if __name__ == "__main__":
    J = Janela ()
    gtk.main ()
