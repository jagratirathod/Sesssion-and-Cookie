from django.contrib.auth.signals import user_logged_in, user_logged_out ,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started ,request_finished , got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("----------------------------------------")
    print("Log-in signal... ")
    print("Sender:",sender) 
    print("Request:",request)
    print("User:",user)
    print("Password:",user.password)
    print(f'kwargs:{kwargs}')

@receiver(user_logged_out,sender=User)  
def log_out(sender,request,user,**kwargs):
    print("----------------------------------------")
    print("Log-out signal... ")
    print("Sender:",sender) 
    print("Request:",request)
    print("User:",user)
    print("Password:",user.password)
    print(f'kwargs:{kwargs}')
 
    # user_logged_in.connect(login_success,sender=User)
    
@receiver(user_login_failed)
def login_failed(sender,credentials,request,user,**kwargs):
    print("----------------------------------------")
    print("Login Failed signal... ")
    print("Sender:",sender) 
    print("Request:",request)
    print("Credentials:",credentials)
    print("User:",user)
    print("Password:",user.password)
    print(f'kwargs:{kwargs}')

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("----------------------")
    print("Pre save signals")   
    print("Sender:",sender) 
    print("Instance:",instance) 
    print(f'kwargs:{kwargs}')

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("----------------------")
        print("New Records")
        print("Post save signals")
        print("Sender:",sender) 
        print("Instance:",instance)
        print("Created:",created) 
        print(f'kwargs:{kwargs}')
    else:
        print("----------------------")
        print("update")
        print("Post save signals")
        print("Sender:",sender) 
        print("Instance:",instance)
        print("Created:",created) 
        print(f'kwargs:{kwargs}')

@receiver(pre_delete,sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print("----------------------")
    print("Pre-Delete signal")   
    print("Sender:",sender) 
    print("Instance:",instance) 
    print(f'kwargs:{kwargs}')

@receiver(post_delete,sender=User)
def at_end_delete(sender,instance,**kwargs):
    print("----------------------")
    print("Post-Delete signal")   
    print("Sender:",sender) 
    print("Instance:",instance) 
    print(f'kwargs:{kwargs}')

@receiver(pre_init,sender=User)
def at_beginning_init(sender,*args,**kwargs):
    print("----------------------")
    print("Pre Init signal")   
    print("Sender:",sender) 
    print(f'kwargs:{kwargs}')
    print(f'Args:{args}')

@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("----------------------")
    print("Post Init signal")   
    print("Sender:",sender) 
    print(f'kwargs:{kwargs}')
    print(f'Args:{args}')


@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
    print("----------------------------------------")
    print("At beginning request")
    print("Sender:",sender) 
    print("Environ:",environ) 
    print(f'kwargs:{kwargs}')

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("----------------------------------------")
    print("At Ending request")
    print("Sender:",sender) 
    print(f'kwargs:{kwargs}')

@receiver(request_finished)
def at_req_exception(sender,request,**kwargs):
    print("----------------------------------------")
    print("At Request exception ")
    print("Sender:",sender) 
    print(f'kwargs:{kwargs}')

@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("----------------------------------------")
    print("Before install app")
    print(f'kwargs:{kwargs}')
    print("Sender:",sender)
    print("App_config",app_config)
    print("Verbosity",verbosity)
    print("Using",using)
    print("Interactive",interactive)
    print("Plan",plan)
    print("Apps",apps)

@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("----------------------------------------")
    print("After install app")
    print(f'kwargs:{kwargs}')
    print("Sender:",sender)
    print("App_config",app_config)
    print("Verbosity",verbosity)
    print("Using",using)
    print("Interactive",interactive)
    print("Plan",plan)
    print("Apps",apps)


@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("----------------------------------------")
    print("Initial connection to database")
    print(f'kwargs:{kwargs}')
    print("Sender:",sender)
    print("connection",connection)







