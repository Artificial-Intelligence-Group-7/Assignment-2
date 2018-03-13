

def Cpt_amenities(con_amenities):
    p_amenities = {}
    p_amenities = {'lots':0.3, 'little':0.7}
    return  p_amenities[con_amenities]

def Cpt_neighborhood(con_neighborhood):
    p_neighborhood = {}
    p_neighborhood = {'bad':0.4, 'good':0.6}
    return p_neighborhood[con_neighborhood]

def Cpt_location(con_location,amenities,neighborhood):
    p_location= {}
    if amenities == 'lots' and neighborhood == 'bad':
        p_location = {'good':0.3, 'bad':0.4, 'ugly':0.3}
    elif amenities == 'lots' and neighborhood == 'good':
        p_location = {'good':0.8, 'bad':0.15, 'ugly':0.05}
    elif amenities == 'little' and neighborhood == 'bad':
        p_location = {'good':0.2, 'bad':0.4, 'ugly':0.4}
    elif amenities == 'little' and neighborhood == 'good':
        p_location = {'good':0.5, 'bad':0.35, 'ugly':0.15}
    return p_location[con_location]

def Cpt_children(con_children,neighborhood):
    p_children ={}
    if neighborhood == 'bad':
        p_children = {'bad':0.6, 'good':0.4}
    elif neighborhood == 'good':
        p_children = {'bad':0.3, 'good':0.7}
    return p_children[con_children]

def Cpt_size(con_size):
    p_size = {}
    p_size = {'small':0.33 , 'medium':0.34, 'large':0.33}
    return p_size[con_size]

def Cpt_schools(con_schools,children):
    p_schools = {}
    if children == 'bad':
        p_schools = {'bad':0.7, 'good':0.3}
    elif children == 'good':
        p_schools = {'bad':0.2, 'good':0.8}

def Cpt_ age(con_age,location):
    p_age = {}
    if location =='good':
        p_age = {'old':0.3, 'new':0.7}
    elif location =='bad':
        p_age = {'old':0.6, 'new':0.4}
    elif location =='ugly':
        p_age = {'old':0.9, 'new':0.1}
    return p_age[con_age]

def Cpt_price(con_price,location,age,schools,size):
    p_price = {}
    # 40
    if location == 'good' and age == 'old' and schools == 'bad' and size =='small':
        p_price = {'cheap':0.5 ,'ok':0.4, 'expensive':0.1}
    # 41
    elif location == 'good' and age == 'old' and schools == 'bad' and size =='medium':
        p_price = {'cheap':0.4 ,'ok':0.45, 'expensive':0.15}
    # 42
    elif location == 'good' and age == 'old' and schools == 'bad' and size =='large':
        p_price = {'cheap':0.35 ,'ok':0.45, 'expensive':0.2}
    # 43
    elif location == 'good' and age == 'old' and schools == 'good' and size =='small':
        p_price = {'cheap':0.4 ,'ok':0.3, 'expensive':0.3}
        # 44
    elif location == 'good' and age == 'old' and schools == 'good' and size =='medium':
        p_price = {'cheap':0.35 ,'ok':0.3, 'expensive':0.35}
        # 45
    elif location == 'good' and age == 'old' and schools == 'good' and size =='large':
        p_price = {'cheap':0.3 ,'ok':0.25, 'expensive':0.45}
        # 46
    elif location == 'good' and age == 'new' and schools == 'bad' and size =='small':
        p_price = {'cheap':0.45 ,'ok':0.4, 'expensive':0.15}
        # 47
    elif location == 'good' and age == 'new' and schools == 'bad' and size =='medium':
        p_price = {'cheap':0.4 ,'ok':0.45, 'expensive':0.15}
        # 48
    elif location == 'good' and age == 'new' and schools == 'bad' and size =='large':
        p_price = {'cheap':0.35 ,'ok':0.45, 'expensive':0.2}
        # 49
    elif location == 'good' and age == 'new' and schools == 'good' and size =='small':
        p_price = {'cheap':0.25 ,'ok':0.3, 'expensive':0.45}
        # 50
    elif location == 'good' and age == 'new' and schools == 'good' and size =='medium':
        p_price = {'cheap':0.2 ,'ok':0.25, 'expensive':0.55}
        # 51
    elif location == 'good' and age == 'new' and schools == 'good' and size =='large':
        p_price = {'cheap':0.1 ,'ok':0.2, 'expensive':0.7}
        # 52
    elif location == 'bad' and age == 'old' and schools == 'bad' and size =='small':
        p_price = {'cheap':0.7 ,'ok':0.299, 'expensive':0.001}
        # 53
    elif location == 'bad' and age == 'old' and schools == 'bad' and size =='medium':
        p_price = {'cheap':0.65 ,'ok':0.33, 'expensive':0.02}
        # 54
    elif location == 'bad' and age == 'old' and schools == 'bad' and size =='large':
        p_price = {'cheap':0.65 ,'ok':0.32, 'expensive':0.03}
        # 55
    elif location == 'bad' and age == 'old' and schools == 'good' and size =='small':
        p_price = {'cheap':0.55 ,'ok':0.35, 'expensive':0.1}
        # 56
    elif location == 'bad' and age == 'old' and schools == 'good' and size =='medium':
        p_price = {'cheap':0.5 ,'ok':0.35, 'expensive':0.15}
        # 57
    elif location == 'bad' and age == 'old' and schools == 'good' and size =='large':
        p_price = {'cheap':0.45 ,'ok':0.4, 'expensive':0.15}
        # 58
    elif location == 'bad' and age == 'new' and schools == 'bad' and size =='small':
        p_price = {'cheap':0.6 ,'ok':0.35, 'expensive':0.05}
        # 59
    elif location == 'bad' and age == 'new' and schools == 'bad' and size =='medium':
        p_price = {'cheap':0.55 ,'ok':0.35, 'expensive':0.1}
        # 60
    elif location == 'bad' and age == 'new' and schools == 'bad' and size =='large':
        p_price = {'cheap':0.5 ,'ok':0.4, 'expensive':0.1}
        # 61
    elif location == 'bad' and age == 'new' and schools == 'good' and size =='small':
        p_price = {'cheap':0.4 ,'ok':0.4, 'expensive':0.2}
        # 62
    elif location == 'bad' and age == 'new' and schools == 'good' and size =='medium':
        p_price = {'cheap':0.3 ,'ok':0.4, 'expensive':0.3}
        # 63
    elif location == 'bad' and age == 'new' and schools == 'good' and size =='large':
        p_price = {'cheap':0.3 ,'ok':0.3, 'expensive':0.4}
        # 64
    elif location == 'ugly' and age == 'old' and schools == 'bad' and size =='small':
        p_price = {'cheap':0.8 ,'ok':0.1999, 'expensive':0.0001}
        # 65
    elif location == 'ugly' and age == 'old' and schools == 'bad' and size =='medium':
        p_price = {'cheap':0.75 ,'ok':0.24, 'expensive':0.01}
        # 66
    elif location == 'ugly' and age == 'old' and schools == 'bad' and size =='large':
        p_price = {'cheap':0.75 ,'ok':0.23, 'expensive':0.02}
        # 67
    elif location == 'ugly' and age == 'old' and schools == 'good' and size =='small':
        p_price = {'cheap':0.65 ,'ok':0.3, 'expensive':0.05}
        # 68
    elif location == 'ugly' and age == 'old' and schools == 'good' and size =='medium':
        p_price = {'cheap':0.6 ,'ok':0.33, 'expensive':0.07}
        # 69
    elif location == 'ugly' and age == 'old' and schools == 'good' and size =='large':
        p_price = {'cheap':0.55 ,'ok':0.37, 'expensive':0.08}
        # 70
    elif location == 'ugly' and age == 'new' and schools == 'bad' and size =='small':
        p_price = {'cheap':0.7 ,'ok':0.27, 'expensive':0.03}
        # 71
    elif location == 'ugly' and age == 'new' and schools == 'bad' and size =='medium':
        p_price = {'cheap':0.64 ,'ok':0.3, 'expensive':0.06}
        # 72
    elif location == 'ugly' and age == 'new' and schools == 'bad' and size =='large':
        p_price = {'cheap':0.61 ,'ok':0.32, 'expensive':0.07}
        # 73
    elif location == 'ugly' and age == 'new' and schools == 'good' and size =='small':
        p_price = {'cheap':0.48 ,'ok':0.42, 'expensive':0.1}
        # 74
    elif location == 'ugly' and age == 'new' and schools == 'good' and size =='medium':
        p_price = {'cheap':0.41 ,'ok':0.39, 'expensive':0.2}
        # 75
    elif location == 'ugly' and age == 'new' and schools == 'good' and size =='large':
        p_price = {'cheap':0.37 ,'ok':0.33, 'expensive':0.3}
    return p_price[con_price]
