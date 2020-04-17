from flask import Flask, render_template

products = {
  "sku01": {
    "id": "sku01", 
    "name": "Pen", 
    "price": 15, 
    "desc": "This is a pen.", 
    "picture": "https://cdn11.bigcommerce.com/s-b17f1zdab8/images/stencil/1280x1280/products/257/678/117808_AT0112-18_Calais_Matte_Metallic_Blue_BP_01__94974.1541480028.jpg?c=2&imbypass=on"
    },
  
  "sku02": {
    "id": "sku02", 
    "name": "Cup", 
    "price": 80, 
    "desc": "This is a cup.",
    "picture": "https://dictionary.cambridge.org/fr/images/thumb/cup_noun_002_09489.jpg?version=5.0.75"
    },
  
  "sku03": {
    "id": "sku03", 
    "name": "Notebook", 
    "price": 25, 
    "desc": "great notebook",
    "picture": "https://poppin.imgix.net/products/2018/Medium-Spiral-Notebook_Storm-Velvet_PDP_02.jpg"
    },
  
  "sku04": {
    "id": "sku04", 
    "name": "Stapler", 
    "price": 20, 
    "desc": "useful stapler",
    "picture": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUQERMQFhUTFRUVGBESEhEXFRUXFRUWFhUZFxUaHSggGBolGxUXIT0iKSkrLi4uFx8zODMtNygtLysBCgoKDQ0NDg8PFTgZFR0rKyw3KysrLSs3MCsrKyssLSsrLSsrKys4LS0rKystKystKystKy0rKystLS0rKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABgIDBAUHAQj/xAA/EAACAQIEAgcDCQcEAwAAAAAAAQIDEQQFITESQQYHE1FhcYEiUpEjMmJygqGxwdEzQkOSouHwFFNj8XOywv/EABYBAQEBAAAAAAAAAAAAAAAAAAABAv/EABcRAQEBAQAAAAAAAAAAAAAAAAARAQL/2gAMAwEAAhEDEQA/AO4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAegAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGtxvSDCUf2uJw8H7sqsOL+W9wNkCJ4jrGy2OirSl9SlVf3tJGFPrSwS2hipeKhT/OaAnIITS6zsHJ6wxMfFwp/lNm0w3TfAT/AI3C+6cKkfvat94EiBawuJhUip05xnF7Si018UXQAAAAAAAAAAAAAAAAAAAAGtzfP8LhVfEV6VPmoykuN/Vgval6IDZA5tmfW5R4lTwdCpWnJqMZVGqUG27Kyd5PXvUSG5x0vzfFSdNSdNNN8GGtCPDZO7q3btaS14ktQO54zHUqS4qtSnTXvVJxivi2RnMusnLaN12/aP3aMJTv5TtwfecEx+ClTalOVNymlKSU1KonJXtUT9pS7795i3A67mPXJHbD4WT+lWqKP9EL3/mIzmHWdmVXSNSnSXdSpr8Z8TIZGBeskrvReP5LmBl43OMTW/bV69S/KdSbj/K3ZGGpJFmpmNNbRk/rOy+C/UtPNJfuqMfqxV/juBsIp8k/PZfFh1rbuC+1f8DS1cTKW7b82WO114Vdvuim2USD/X/TXpFnsc2a/e/p/uaNU5v3Y+b4n8I6feVLD98pvytFfm/vAleVdMK+Hlx0p8L52uk/NXafqjpfQzrOeJrU8LXpRU6j4Y1actL2b9qDWm26focOpYVNqMY3baSTcndvRbuxn4nCVcHX4fZhVptNVKLjdNq94zjrztdeJB9Vg0PQXOHi8DQryd5uPDN984Nwm7crtX9TfAAAAAAAAAAAAAMDPsVKlhq9WHzqdGpON/ejBuOnmkB5m+eYbCx4sTWpU09lOS4pfVjvL0RAs664cPC8cJRqVX79T5OHmlrJ+TSOO42pOU5TqylOpJ3dSbblJ/Sb38zHUgJ5jummOxcbzxcaUZNpUMLKnTlvbWUpqav4OV+40NfKIQnKVatGKvxcM05Vpp3a4oR2bs9b/ir63DYqqo8NNuKe8oKMZPwdRWbXhexbhTTdleT7oL/6elwNj/rcPTt2NFzkv4ld8/8Axp2svO/O/IpzHM61ZyblKNOTvwtpRSatq0lx6JK7u7JFtYSUdZunSX0nefotWvhYs1MTh4apTqy96btG/lv96At0qSbtFSm+6C0+L39EZMsK4/tJwo/RjrU/OS9bGFXzqo1wxahH3YLhXrbV+prpVWwNrLF04+zSUn9Kf6fq2YtWo3q3cxaTL0mUY0jw9lv56epJck6CY7E2kqXZQf8AEr3hp4Qtxv4W8QIyjzLI6OXeyW9PeiEcuw1KarTqVKlTgk+GMYJKEm+GOrve2rZFcE7U033NgZiFy0qhTKqBk0qzi1Jbxaa81qhjcZKpN1Ju8pbv7kku6ysaypjkttfwLVOVSrLhim/BbAd16g8xlKnisO0+GEqdVPknUUoyXh+yi/VnWT5u6CZ1WyurF9peNSce1oNuzi7JtR5TS1T0bslsfSJAAAAAAAAAAAA0vTSpw4HEv/ikv5lw/mbojPWTU4cur+PZr41YX+64Hz5m/wA5eRgWuZ2ZayXkYNR2/wA8GUYdHHyc0paq+q7l3L9TZV84ntC0F9DR/Hd/E0yepXcC5Oo3q2ylspFgPbi5kYDL6taXBRp1KkvdpxcmvO2y8WTjJOqrFVbSxM4UI6ezpUqeVk+Fed35AQSgm2krttpJJXbb0SS5s6F0b6sq9dKpipOhB68CSdZryekPW78CfdHOiGCwNpUoOVW1u2qtSqePDpaH2Ui7m3SqhSvHic5r+HStKSfc3fhh9pozRaynozhMI/kKUFJadrP2qj7/AG3ql4Ky8C/mudUMNHjr1YU1y4n7T+rFay9EQrPOluIcJzhalGMZStB8VSVk2k5tWjfuir+Jx7G4udWbqTcpSe8pSlJ/GTb+8KnXWP0qpZhCEaKkoUXKfHOylNtKKtG/srffXwIjQg5QUVa7TerSXN7s18/mr2nfnG23c78yulCUmkrt7WRpF2piraL+xbhTnUdkm2+S/Q21LJo01xYiXDzVOOs36cvuLrzPgXDQiqa97eb85cvQC3RyKNNcWJmo/wDGtZv05F2pmCiuChFU49+839rl6GTkvRzFYt3hF8L/AIk729Ocjp/Rnq0o0rTrfKSWvtbJ+EdvxIIb1fdDKmNrKdSTpUotS45RbdRpp8ML23V/a5dzPo80+X4GMbKKSS7vA3AAAAAAAAAAAADT9LMmeMw08Op8DdnGTV1xRd0peHl/Y3AA+XukWXVcPXdGtBwnFLR81ycX+9HxRqK60fk/wPpDpZgqVaahVpwmuFaTinbWW19n5ELq9X2ClPitWUedJVPZfq05L+YUcSUNTZ5VkOKxP7CjUmtuJK0F5zlaKfhc6/h+rvL4cM3TqSvJrhnVlw7SeytfY2EM6owqU8HhqM5pPhk6EEqNCMW1JznpFNO64Vd3Vtyb0uZuoBlnVTiJ6161Kn9GCdSVvO8Un6sluVdWeBpWdTtKzWvys7R/lgkmvB3JFj80pUI8VWpGCeyb9qX1YrWT8kRbMOmspezh6dl/uVvypp/i15CiZ0o0MPT4YRpUqcVtFRhCP5I0+I6T8fF/pKVSvw7zjGSpLznZt/ZTXiQTEV51nxVpyqNariatH6sF7MfNI1WYdJpUPZw+IrRd7uFJwdNvvlxRevkBJMwzTEVr9rUajzp0704fa14pert4IjOYZ/SprgpJTa0tGygvXn6Eax2bVqulSba7tk/F23ZiU6cpbL9F6iDIzHM51Pny091aRXoayjhpT+atPee3x5vwWpv6GUqKU60oxj3yvr9WHzp/h3ntXNow0w8LW07WaTl9mPzYL4lRjUsiUUp4iapw5Jr25fVjvb/NC5LMYwXDh4cC992dR+u0fTXxGW5VicZP5OM5tvWcr2XnJ/8AZ0zov1Wwjapinxy34NoL0/e9fgBzjJsgxOLl8lCTTetSV1H48/S51Dox1Y0qdp1/lJb2a9leUf1udCwOWQppRhFJLuRnwpAYODy6FNWjFIzoUy9GmXYQArpwsisAAAAAAAAAAAU1KiinKTSSTbk2kklu2+SAqPG7akEz/rMoUk1hY9u1p2jfDST8HvP0Vn3kXwHWLKVVxx0ZOL1UqdlGn4dju1zvrLUDoudOFWzpS+UVrStem13N3V93qr2I/hsyjKfZtwUtV7NSM4ykt1GS0bVndO0lba2ptqGLhVpdph5U6ia9l8Vo37pNJuPwKcXJWcfk1PdKok0+Gz79fO+lyC1xpqKV2078Md/3o69y1fwI10xxmMpR+ShKFPd1ocMn4pqz4PP4Mu4rpTTwcGputN3ulUVLnfRThaKSdvHfch+cdK6tdNSrYmnK+lOEIwhFa3u+Liltblz32CtY5tycpOUpPecm5SfnJ6sx8Xm9Olu7y92P68ih4avXfZx4uLfjgklbvk3ZcL73b1IrWoyU5Qdm4ycW4u6fC7NqXdpuBm5hnNSrpfhj7sfz7zBpxb0S/wA8zPw2UtrjqNQh7020vTnJ+CL08wpUtKEeJr+JUS/phsvX4FR5hspsu0qtQj707pPyXzpPyKquZwp6UI3a/iVEv6YbR+8xsPh8Ri6loRqVZv1t5vaKOidGOqtu08XK/Ps4XUfWW79LAc9wWAxGLqWpxnUk95O9l5yeiOk9GOqtaTxb4nv2cbqC8+cvu8jpeVZHSoRUKcIxS2SSSNtCiBrMtyelRio04RSWiSSSNnCkXo0y5GAFqNMuqBWolVgKVEqSPQAAAAAAAAAAAA5n15ZjOGHo4eLajXnKU7O11S4WovwvJP7KOmEV6wujFLHYe85OFSipyp1L6JtK8ZLnF2j46K3iHz2sU38/4l2KT1uWKsXFuM4tNbp6NFEW1qmUbjLs2rYWXaUZyjLuTupJcpLVNeae5IcP1hqulDE2hPldpUm+dnbT7W2lm3oQitinwO2/Lu8zTQcovidpPu33/Pcg7TWoU8VQdGfFKKtpq3FrVNSfzWvFpojGIwVCMpTq1Z4iS5cSjBLV/KVb67t6W1vqR/LJ1owce0n2KVlGpUnGkrO/zb6+SLGLzWC+b8pJbSmrU4/Upr8WIrfYrNpShaHBCkuduzor6sfnTf8AmpHKmYUqbfZRU5Xb7ScUo3fONP8AN/AwpTrYiaj7dSb0jGKbfpFbInfRjqtq1bTxTcI79lBpy+1LZel/MIg1OnXxVThiqlWb5LWy/CK+COg9GOquc7TxcrL/AGoP/wBp/p8TqORdGKGGioUqcYrwW77292/Fm+p0bAaXJuj1HDxUKcIxS5JJf9s3VOiX40y4oAWo0y6oFaR6BSolVgAAAAAAAAAAAAAAAAABrc9wrqQSWyeq/A2QaA5Tn/RaFXeKv32Oe5x0Zq0buKckuXP07z6LxeXxkaLGZKno0FfOb18zBVdxqXSi0u+K3t+p23OOr2lWbnFOMmvnR0+K2Zocv6pJuo3WqrhUlZQTvJLfiv8ANvtpcI5lXxFSrJKTlJvSMUm/JRivwRM+jPVpiMRaeIvRg/3dHVa8toet34HWuj/QnC4XWnTipc5vWb+09l4KyJPRwyWyAjXRzofh8JG1KnFd8t5S+tJ6sklKglsZMaZWogW40y4oFVj0DxI9AAAAAAAAAAAAAAAAAAAAAAAAAAFMoJlQAxp4dCNIyTywFtQK1EqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf/9k="
    }
}

cart = {
  "sku01": 2,
  "sku02": 5
}

app = Flask(__name__)

@app.route("/")
def myshop():
    return render_template("myshop.html", products=products, cart=cart)
    

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)