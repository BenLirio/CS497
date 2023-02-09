function bloch_to_ket(theta, phi)
    return cos(theta/2), exp(1im*phi)*sin(theta/2)
end

function ket_to_bloch(a, b)
    theta = 2*acos(a)
    phi = atan(imag(b), real(b))
    return theta, phi
end