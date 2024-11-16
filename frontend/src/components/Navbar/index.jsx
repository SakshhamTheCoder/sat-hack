import React from 'react';
import { useNavigate } from 'react-router-dom';

const Navbar = ({ tranparent = false }) => {
    return (
        <nav className={`flex items-center justify-between p-6 ${tranparent ? 'bg-transparent' : 'bg-black/40'}`}>
            <div className="text-2xl font-bold">
                <img
                    src="/logo.jpg"
                    alt="GoSnap"
                    className="h-[3.5rem] w-auto md:h-[3.5rem] rounded-xl "
                    onClick={() => navigate('/')}
                    style={{ cursor: 'pointer' }}
                />
            </div>
            <div className="flex space-x-2 md:space-x-6">
            </div>
        </nav >
    );
};

export default Navbar;